"""Create ARM field-campaign data-availability summary PDFs.

This optimized refactor of AFC_Summary/afc_summary.py uses direct netCDF4 time reads, integer binning, Dask parallelism, and per-file caching. It preserves the
existing configuration-file interface while separating configuration, data
access, availability calculations, and plotting into testable functions.
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import textwrap
import warnings
import re
import hashlib
import os

os.environ.setdefault("HDF5_USE_FILE_LOCKING", "FALSE")
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import act
# netCDF4/HDF5 is used only for direct time-variable reads.
from netCDF4 import Dataset, num2date

try:
    from dask import compute, delayed
except ImportError:  # Optional fallback for environments without Dask.
    compute = None
    delayed = None
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import ListedColormap
from matplotlib.dates import DateFormatter, HourLocator
from scipy import stats


DQR_URL = "https://dqr-web-service.svcs.arm.gov/dqr_qc/{datastream}/incorrect,suspect,missing"
DOI_URL = "https://adc.arm.gov/citationservice/citation/inst-class"
METADATA_URL = "https://adc.arm.gov/elastic/metadata/_search"
OPEN_ENDED_DQR = pd.Timestamp("3001-01-01")
DQR_CODES = {"Suspect": 2, "Incorrect": 3, "Missing": 4}
DQR_COLORS = {2: "yellow", 3: "red", 4: "grey"}
AVAILABILITY_CMAP = ListedColormap(["white", "cornflowerblue", "yellow", "red"])


@dataclass(frozen=True)
class DateRange:
    start: pd.Timestamp
    end: pd.Timestamp

    @property
    def dates(self) -> pd.DatetimeIndex:
        return pd.date_range(self.start, self.end + pd.Timedelta(days=1), freq="D")

    @property
    def start_text(self) -> str:
        return self.start.strftime("%Y-%m-%d")

    @property
    def end_text(self) -> str:
        return self.end.strftime("%Y-%m-%d")


@dataclass(frozen=True)
class Layout:
    nrows: int
    ncols: int
    wrap_width: int
    text_spacing: float
    font_size: int


@dataclass(frozen=True)
class AvailabilityResult:
    index: pd.DatetimeIndex
    data: np.ndarray
    dqr_data: np.ndarray
    time_delta: float


class ArmClient:
    """Small HTTP client for ARM metadata, DOI, and DQR services."""

    def __init__(self, timeout: int = 30, retries: int = 3) -> None:
        self.timeout = timeout
        self.session = requests.Session()

        retry_policy = Retry(
            total=retries,
            connect=retries,
            read=retries,
            status=retries,
            backoff_factor=1.0,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=frozenset({"GET"}),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_policy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def _get_json(self, url: str, **kwargs: Any) -> Any:
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_dqrs(self, datastream: str) -> pd.DataFrame:
        """Return DQR records for a datastream without making 404 fatal.

        The DQR API may return HTTP 404 with ``{"detail": "Not Found"}``
        when no DQRs exist. Any unavailable or malformed DQR response is
        therefore treated as an empty result so report generation can proceed.
        """
        url = DQR_URL.format(datastream=datastream)
        columns = ["dqr_num", "start", "end", "code", "subject"]
        empty = pd.DataFrame(columns=columns)

        try:
            response = self.session.get(url, timeout=self.timeout)
        except requests.RequestException as exc:
            warnings.warn(
                f"Unable to contact the DQR service for {datastream}: {exc}. "
                "Continuing without DQR overlays.",
                RuntimeWarning,
                stacklevel=2,
            )
            return empty

        # The service commonly uses 404 + {"detail": "Not Found"} to mean
        # that there are no matching DQR records. Never call raise_for_status()
        # in this method because that response is expected and non-fatal.
        if response.status_code == 404:
            return empty

        if response.status_code != 200:
            warnings.warn(
                f"DQR service returned HTTP {response.status_code} for "
                f"{datastream}. Continuing without DQR overlays.",
                RuntimeWarning,
                stacklevel=2,
            )
            return empty

        try:
            payload = response.json()
        except (requests.exceptions.JSONDecodeError, ValueError):
            warnings.warn(
                f"DQR service returned invalid JSON for {datastream}. "
                "Continuing without DQR overlays.",
                RuntimeWarning,
                stacklevel=2,
            )
            return empty

        if not isinstance(payload, dict) or payload.get("detail") == "Not Found":
            return empty

        stream_payload = payload.get(datastream, {})
        if not isinstance(stream_payload, dict):
            return empty

        rows: list[dict[str, Any]] = []
        for category, reports in stream_payload.items():
            if not isinstance(reports, dict):
                continue
            for number, report in reports.items():
                if not isinstance(report, dict):
                    continue
                for time_range in report.get("dates", []):
                    if not isinstance(time_range, dict) or "start_date" not in time_range:
                        continue
                    end = time_range.get("end_date")
                    rows.append(
                        {
                            "dqr_num": number,
                            "start": pd.Timestamp(time_range["start_date"]),
                            "end": (
                                OPEN_ENDED_DQR
                                if end in (None, "None")
                                else pd.Timestamp(end)
                            ),
                            "code": category,
                            "subject": report.get("subject", ""),
                        }
                    )

        return pd.DataFrame(rows, columns=columns)

    def get_doi(
        self,
        instrument: str,
        site: str,
        datastream: str,
        date_range: DateRange,
    ) -> str:
        params = {
            "id": instrument,
            "citationType": "apa",
            "site": site,
            "dataLevel": datastream.rsplit(".", 1)[-1],
            "startDate": date_range.start_text,
            "endDate": date_range.end_text,
        }
        try:
            payload = self._get_json(DOI_URL, params=params)
            return payload.get("citation", "N/A")
        except (requests.RequestException, ValueError, AttributeError):
            return "N/A"

    def get_metadata(self, datastream: str, field: str = "instrument_name_text") -> str:
        params = {
            "q": f"datastream:{datastream}",
            "_source": "instrument_name_text,facility_name",
            "filter_path": "hits.hits._source",
            "size": 1,
        }
        try:
            payload = self._get_json(METADATA_URL, params=params)
            source = payload["hits"]["hits"][0]["_source"]
            return source.get(field, datastream)
        except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
            return datastream


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a Python configuration file without using ``exec``."""
    path = Path(path).expanduser().resolve()
    spec = importlib.util.spec_from_file_location("afc_summary_config", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"Unable to load configuration file: {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "conf") or not isinstance(module.conf, dict):
        raise ValueError(f"Configuration file {path} must define a dictionary named 'conf'.")
    return module.conf


def resolve_date_range(conf: dict[str, Any]) -> DateRange:
    if "previous_days" in conf:
        end = pd.Timestamp.today().normalize()
        start = end - pd.Timedelta(days=int(conf["previous_days"]))
    else:
        try:
            start = pd.Timestamp(conf["start_date"])
            end = pd.Timestamp(conf["end_date"])
        except KeyError as exc:
            raise ValueError("Set start_date/end_date or previous_days in the configuration.") from exc

    if end < start:
        raise ValueError("end_date must be on or after start_date.")
    return DateRange(start=start, end=end)


def get_layout(chart_style: str, info_style: str) -> Layout:
    if chart_style == "linear":
        return Layout(
            nrows=20,
            ncols=4,
            wrap_width=25 if info_style == "simple" else 20,
            text_spacing=0.275 if info_style == "simple" else 0.2,
            font_size=9 if info_style == "simple" else 6,
        )
    if chart_style == "2D":
        return Layout(nrows=8, ncols=3, wrap_width=47, text_spacing=0.1, font_size=8)
    raise ValueError("chart_style must be either 'linear' or '2D'.")


def find_files_for_range(
    data_path: str | Path,
    site: str,
    datastream: str,
    date_range: DateRange,
) -> list[str]:
    """Find candidate files using year-specific ARM filename patterns."""
    directory = Path(data_path) / site / datastream
    if not directory.exists():
        return []

    candidates: set[Path] = set()
    for year in range(date_range.start.year, date_range.end.year + 1):
        for suffix in ("nc", "cdf"):
            candidates.update(directory.glob(f"{datastream}.{year}*.{suffix}"))
            candidates.update(directory.glob(f"{datastream}{year}*.{suffix}"))

    # Some nonstandard files do not include the date after a period. Fall back
    # to a full listing only when year-specific patterns found nothing.
    if not candidates:
        for suffix in ("nc", "cdf"):
            candidates.update(directory.glob(f"{datastream}*.{suffix}"))

    selected: list[str] = []
    for path in sorted(candidates):
        matches = re.findall(r"(?<!\d)(\d{8})(?!\d)", path.name)
        if matches:
            try:
                file_date = pd.Timestamp(matches[-1])
            except ValueError:
                file_date = None
            if file_date is not None and not (
                date_range.start <= file_date <= date_range.end
            ):
                continue
        selected.append(str(path))
    return selected


def _cache_path(
    cache_dir: Path,
    path: str,
    stat: os.stat_result,
    start_ns: int,
    end_ns: int,
    delta_ns: int,
) -> Path:
    token = "|".join(
        [
            str(Path(path).resolve()),
            str(stat.st_size),
            str(stat.st_mtime_ns),
            str(start_ns),
            str(end_ns),
            str(delta_ns),
        ]
    )
    digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
    return cache_dir / f"{digest}.npy"


def read_file_bins(
    path: str,
    *,
    start_ns: int,
    end_ns: int,
    delta_ns: int,
    cache_dir: str | None = None,
) -> np.ndarray:
    """Read only ``time`` and return unique occupied output-bin positions."""
    file_path = Path(path)
    stat = file_path.stat()
    cache_path: Path | None = None

    if cache_dir:
        cache_root = Path(cache_dir).expanduser()
        cache_root.mkdir(parents=True, exist_ok=True)
        cache_path = _cache_path(
            cache_root, path, stat, start_ns, end_ns, delta_ns
        )
        if cache_path.exists():
            try:
                return np.load(cache_path, allow_pickle=False)
            except (OSError, ValueError):
                cache_path.unlink(missing_ok=True)

    with Dataset(path, mode="r") as nc:
        if "time" not in nc.variables:
            bins = np.array([], dtype=np.int64)
        else:
            variable = nc.variables["time"]
            values = variable[:]
            if values.size == 0:
                bins = np.array([], dtype=np.int64)
            else:
                decoded = num2date(
                    values,
                    units=variable.units,
                    calendar=getattr(variable, "calendar", "standard"),
                    only_use_cftime_datetimes=False,
                    only_use_python_datetimes=True,
                )
                times_ns = np.asarray(decoded, dtype="datetime64[ns]").astype(np.int64)
                valid = (times_ns >= start_ns) & (times_ns < end_ns)
                bins = np.unique((times_ns[valid] - start_ns) // delta_ns).astype(
                    np.int64, copy=False
                )

    if cache_path is not None:
        temporary = cache_path.with_suffix(f".{os.getpid()}.tmp.npy")
        try:
            np.save(temporary, bins, allow_pickle=False)
            os.replace(temporary, cache_path)
        except OSError:
            temporary.unlink(missing_ok=True)

    return bins


def read_occupied_bins(
    files: Iterable[str],
    *,
    start_ns: int,
    end_ns: int,
    delta_ns: int,
    use_dask: bool = True,
    workers: int | None = None,
    scheduler: str = "threads",
    cache_dir: str | None = None,
) -> list[np.ndarray]:
    """Read occupied bins from files, optionally in parallel."""
    paths = list(files)
    if not paths:
        return []

    kwargs = {
        "start_ns": start_ns,
        "end_ns": end_ns,
        "delta_ns": delta_ns,
        "cache_dir": cache_dir,
    }
    if use_dask and delayed is not None and compute is not None and len(paths) > 1:
        tasks = [delayed(read_file_bins)(path, **kwargs) for path in paths]
        return list(
            compute(
                *tasks,
                scheduler="threads",
                num_workers=max(1, int(workers or min(8, len(tasks)))),
            )
        )
    return [read_file_bins(path, **kwargs) for path in paths]


def normalize_time_delta(time_delta: int | float | None) -> tuple[float, pd.Timedelta]:
    """Normalize a configured interval expressed in minutes.

    Configuration files remain unchanged: ``t_delta`` is still an int or float
    representing minutes. The pandas Timedelta is created only for internal
    indexing and resampling operations.
    """
    value = 1.0 if time_delta is None else time_delta
    try:
        minutes = float(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(
            "t_delta must be an int or float representing minutes"
        ) from exc

    if not np.isfinite(minutes) or minutes <= 0:
        raise ValueError("t_delta must be a finite number greater than zero")

    return minutes, pd.to_timedelta(minutes, unit="min")



def get_configured_time_delta(options: dict[str, Any]) -> int | float | None:
    """Return instrument time resolution in minutes.

    Supports the historical AFC Summary key ``override_delta`` as well as
    ``t_delta`` and ``delta_t``. This preserves existing configuration files.
    """
    for key in ("t_delta", "delta_t", "override_delta"):
        value = options.get(key)
        if value is not None:
            return value
    return None

def make_expected_index(
    date_range: DateRange,
    frequency: pd.Timedelta,
) -> pd.DatetimeIndex:
    """Create one continuous campaign timeline at the requested resolution."""
    return pd.date_range(
        date_range.start,
        date_range.end + pd.Timedelta(days=1),
        freq=frequency,
        inclusive="left",
    )


def apply_dqrs(index: pd.DatetimeIndex, dqrs: pd.DataFrame, campaign_end: pd.Timestamp) -> np.ndarray:
    flags = np.full(len(index), np.nan)
    if dqrs.empty:
        return flags

    for row in dqrs.itertuples(index=False):
        end = campaign_end + pd.Timedelta(days=1) if row.end >= pd.Timestamp("3000-01-01") else row.end
        mask = (index >= row.start) & (index < end)
        code = DQR_CODES.get(row.code)
        if code is not None:
            flags[mask] = code
    return flags


def calculate_availability(
    *,
    site: str,
    datastream: str,
    secondary_datastream: str | None,
    data_path: str | Path,
    time_delta: int | float | None,
    date_range: DateRange,
    dqrs: pd.DataFrame,
    use_dask: bool = True,
    workers: int | None = None,
    scheduler: str = "threads",
    cache_dir: str | None = None,
) -> AvailabilityResult:
    """Calculate continuous availability using integer time-bin positions."""
    time_delta_minutes, frequency = normalize_time_delta(time_delta)
    expected = make_expected_index(date_range, frequency)
    start_ns = int(expected[0].value)
    end_ns = int((date_range.end + pd.Timedelta(days=1)).value)
    delta_ns = int(frequency.value)
    availability = np.zeros(len(expected), dtype=np.uint8)

    streams = [datastream]
    if secondary_datastream:
        streams.append(secondary_datastream)

    for stream in streams:
        files = find_files_for_range(data_path, site, stream, date_range)
        occupied_sets = read_occupied_bins(
            files,
            start_ns=start_ns,
            end_ns=end_ns,
            delta_ns=delta_ns,
            use_dask=use_dask,
            workers=workers,
            scheduler="threads",
            cache_dir=cache_dir,
        )
        for occupied in occupied_sets:
            valid = occupied[(occupied >= 0) & (occupied < len(availability))]
            availability[valid] = 1

    dqr_data = apply_dqrs(expected, dqrs, date_range.end)
    return AvailabilityResult(expected, availability, dqr_data, time_delta_minutes)


def plot_2d(axis: plt.Axes, date_range: DateRange, result: AvailabilityResult) -> None:
    frequency = pd.to_timedelta(result.time_delta, unit="min")
    periods_exact = pd.Timedelta(days=1) / frequency
    if not float(periods_exact).is_integer():
        raise ValueError(
            "For a 2D day/time plot, t_delta must divide evenly into 24 hours. "
            f"Received {result.time_delta} minutes."
        )
    periods_per_day = int(periods_exact)
    n_days = len(pd.date_range(date_range.start, date_range.end, freq="D"))
    expected_size = n_days * periods_per_day
    if len(result.data) != expected_size:
        raise ValueError("Continuous availability timeline cannot be reshaped into complete days.")

    dates = pd.date_range(date_range.start, date_range.end, freq="D")
    times = pd.date_range("2000-01-01", periods=periods_per_day, freq=frequency)
    data = result.data.reshape(n_days, periods_per_day)
    dqr = result.dqr_data.reshape(n_days, periods_per_day)

    axis.pcolormesh(dates, times, data.T, vmin=0, vmax=3, cmap=AVAILABILITY_CMAP, shading="auto")
    axis.pcolor(dates, times, dqr.T, hatch="/", alpha=0)
    axis.yaxis.set_major_locator(HourLocator(interval=6))
    axis.yaxis.set_major_formatter(DateFormatter("%H:%M"))


def mask_to_broken_bar_ranges(
    index: pd.DatetimeIndex,
    mask: np.ndarray,
    time_delta_minutes: float,
) -> list[tuple[np.datetime64, np.timedelta64]]:
    """Convert occupied bins to ``broken_barh`` ranges.

    Runs are split whenever bins are nonadjacent or cross a UTC date boundary.
    Each occupied bin receives at least one full ``t_delta`` of display width,
    so isolated observations remain visible.
    """
    occupied_indices = np.flatnonzero(np.asarray(mask, dtype=bool))
    if occupied_indices.size == 0:
        return []

    occupied_times = index[occupied_indices]
    adjacent = np.diff(occupied_indices) == 1
    same_day = (
        occupied_times[:-1].normalize().to_numpy()
        == occupied_times[1:].normalize().to_numpy()
    )

    breaks = np.flatnonzero(~(adjacent & same_day)) + 1
    groups = np.split(occupied_indices, breaks)

    times = index.to_numpy(dtype="datetime64[ns]")
    delta_ns = int(pd.to_timedelta(time_delta_minutes, unit="min").value)

    return [
        (
            times[group[0]],
            np.timedelta64(int(len(group) * delta_ns), "ns"),
        )
        for group in groups
    ]

def plot_linear(axis: plt.Axes, result: AvailabilityResult) -> None:
    ranges = mask_to_broken_bar_ranges(
        result.index,
        result.data > 0,
        result.time_delta,
    )
    if ranges:
        axis.broken_barh(ranges, (0, 1), facecolors="green")

    for code, color in DQR_COLORS.items():
        ranges = mask_to_broken_bar_ranges(
            result.index,
            result.dqr_data == code,
            result.time_delta,
        )
        if ranges:
            axis.broken_barh(ranges, (0, 1), facecolors=color)

    axis.set_ylim(0, 1)
    axis.get_yaxis().set_visible(False)


def add_cover(fig: plt.Figure, grid: Any, row: int, title: str) -> int:
    axis = fig.add_subplot(grid[row, :])
    axis.axis("off")
    axis.text(0.5, 0.99, "\n".join(textwrap.wrap(title, width=70)), size=14, ha="center")
    axis.text(0.5, 0.45, "Atmospheric Radiation Measurement User Facility", size=12, ha="center")
    return row + 2


def add_instrument_text(
    axis: plt.Axes,
    *,
    instrument: str,
    description: str,
    datastreams: list[str],
    doi: str,
    info_style: str,
    include_doi: bool,
    layout: Layout,
) -> None:
    axis.axis("off")
    y = 0.95
    ds_text = "\n".join(textwrap.wrap(", ".join(datastreams), width=layout.wrap_width))

    if info_style == "simple":
        axis.text(0, y, instrument.upper(), size=layout.font_size, va="top", weight="bold")
        y -= layout.text_spacing
        axis.text(0, y, ds_text, size=layout.font_size, va="top")
        return

    wrapped_description = "\n".join(textwrap.wrap(description, width=layout.wrap_width))
    axis.text(0, y, wrapped_description, size=layout.font_size, va="top")
    y -= layout.text_spacing * (1 + max(0, len(description) // layout.wrap_width))
    axis.text(0, y, f"ARM Name: {instrument.upper()}", size=layout.font_size, va="top")
    y -= layout.text_spacing
    axis.text(0, y, f"Datastream: {ds_text}", size=layout.font_size, va="top")
    y -= layout.text_spacing * (1.1 + max(0, len(ds_text) // layout.wrap_width))
    if include_doi:
        axis.text(0, y, "\n".join(textwrap.wrap(doi, width=layout.wrap_width)), size=layout.font_size, va="top")



def add_table_pages(
    pdf: PdfPages,
    *,
    title: str,
    headers: list[str],
    rows: list[list[Any]],
    rows_per_page: int,
    column_widths: list[float],
    font_size: int,
    scale: float,
) -> None:
    for start in range(0, len(rows), rows_per_page):
        fig, axis = plt.subplots(figsize=(8.27, 11.69), dpi=100)
        axis.axis("off")
        axis.set_title(title)
        table = axis.table(
            cellText=rows[start : start + rows_per_page],
            colLabels=headers,
            loc="best",
            colWidths=column_widths,
            cellLoc="left",
        )
        table.auto_set_font_size(False)
        table.set_fontsize(font_size)
        table.scale(1, scale)
        fig.subplots_adjust(top=0.95, left=0.02, right=0.98)
        pdf.savefig(fig)
        plt.close(fig)


def create_summary(conf: dict[str, Any]) -> None:
    site = conf["site"]
    instruments = conf["instruments"]
    output = conf.get("outname", "afc_summary.pdf")
    base_data_path = conf.get("data_path", "/data/archive")
    chart_style = conf.get("chart_style", "2D")
    info_style = conf.get("info_style", "complex")
    date_range = resolve_date_range(conf)
    layout = get_layout(chart_style, info_style)
    client = ArmClient(timeout=int(conf.get("http_timeout", 30)))

    dqr_rows: list[list[Any]] = []
    doi_rows: list[list[Any]] = []
    row = 0
    shared_axis: plt.Axes | None = None
    fig: plt.Figure | None = None
    grid = None

    with PdfPages(output) as pdf:
        for number, (instrument, options) in enumerate(instruments.items()):
            if row == 0:
                fig = plt.figure(figsize=(8.27, 11.69), constrained_layout=True, dpi=100)
                grid = fig.add_gridspec(layout.nrows, layout.ncols)

            datastream = site + options["dsname"]
            secondary = site + options["dsname2"] if options.get("dsname2") else None
            data_path = options.get("data_path", base_data_path)
            print(datastream)

            dqrs = client.get_dqrs(datastream)
            if conf.get("dqr_table", False) and not dqrs.empty:
                for report in dqrs.drop_duplicates("dqr_num").itertuples(index=False):
                    dqr_rows.append(
                        [datastream, report.dqr_num, report.code, "\n".join(textwrap.wrap(report.subject, 50)), report.start, report.end]
                    )

            if number == 0:
                facility = client.get_metadata(datastream, field="facility_name")
                row = add_cover(fig, grid, row, facility)

            use_dask = bool(conf.get("use_dask", True))
            if use_dask and delayed is None:
                warnings.warn(
                    "Dask is not installed; falling back to serial processing.",
                    RuntimeWarning,
                    stacklevel=2,
                )
                use_dask = False

            configured_delta = get_configured_time_delta(options)
            print(f"  time delta: {configured_delta if configured_delta is not None else 1.0} minutes")

            result = calculate_availability(
                site=site,
                datastream=datastream,
                secondary_datastream=secondary,
                data_path=data_path,
                time_delta=get_configured_time_delta(options),
                date_range=date_range,
                dqrs=dqrs,
                use_dask=use_dask,
                workers=int(conf.get("dask_workers", 4)),
                scheduler=str(conf.get("dask_scheduler", "threads")),
                cache_dir=(
                    None
                    if conf.get("cache_dir", "~/.cache/afc_summary") is None
                    else str(conf.get("cache_dir", "~/.cache/afc_summary"))
                ),
            )

            doi = client.get_doi(instrument, site, options["dsname"], date_range)
            if conf.get("doi_table", False):
                doi_rows.append([instrument.upper(), "\n".join(textwrap.wrap(doi, width=90))])

            description = client.get_metadata(datastream)
            text_axis = fig.add_subplot(grid[row, 0])
            add_instrument_text(
                text_axis,
                instrument=instrument,
                description=description,
                datastreams=[item for item in (datastream, secondary) if item],
                doi=doi,
                info_style=info_style,
                include_doi=not conf.get("doi_table", False),
                layout=layout,
            )

            plot_axis = fig.add_subplot(grid[row, 1:], rasterized=True, sharex=shared_axis)
            shared_axis = shared_axis or plot_axis
            if chart_style == "2D":
                plot_2d(plot_axis, date_range, result)
            else:
                plot_linear(plot_axis, result)

            if number == 0 or row == 0:
                plot_axis.xaxis.tick_top()
                plot_axis.tick_params(axis="x", labelsize=8)
            else:
                plot_axis.get_xaxis().set_visible(False)
            plot_axis.set_xlim(date_range.start, date_range.end + pd.Timedelta(days=1))

            row += 1
            if row >= layout.nrows:
                pdf.savefig(fig)
                plt.close(fig)
                fig = None
                grid = None
                row = 0
                shared_axis = None

        if fig is not None:
            pdf.savefig(fig)
            plt.close(fig)

        if conf.get("dqr_table", False):
            add_table_pages(
                pdf,
                title="ARM Data Quality Report (DQR) Table",
                headers=["Datastream", "DQR", "Quality", "Subject", "Start Date", "End Date"],
                rows=dqr_rows,
                rows_per_page=30,
                column_widths=[0.165, 0.085, 0.08, 0.35, 0.145, 0.145],
                font_size=7,
                scale=1.7,
            )

        if conf.get("doi_table", False):
            rows_per_page, scale = (13, 4) if site == "bnf" else (17, 3)
            add_table_pages(
                pdf,
                title="ARM Data Object Identifier (DOI) Table",
                headers=["Instrument", "DOI"],
                rows=doi_rows,
                rows_per_page=rows_per_page,
                column_widths=[0.15, 0.8],
                font_size=8,
                scale=scale,
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create campaign summary plots.")
    parser.add_argument("-c", "--conf", required=True, help="Python configuration file defining 'conf'.")
    return parser.parse_args()


def main() -> None:
    started = pd.Timestamp.now()
    args = parse_args()
    create_summary(load_config(args.conf))
    print(pd.Timestamp.now() - started)


if __name__ == "__main__":
    main()
