# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'epc',
    'facility': 'M1',
    'start_date': '2023-02-15',
    'end_date': '2024-02-14',
    'outname': '/home/theisen/Code/AFC_Summary/images/epc/epc_S2_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    "export_table": True,
    "export_frequency": "monthly",
    "export_metric": "percent_good",
    "cache_dir": "~/.cache/afc_summary",
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'ceil': {'dsname': 'ceilS2.b1'},
        'dl': {'dsname': 'dlfptS2.b1', 't_delta': 60},
        'kasacr': {'dsname': 'kasacrcfrqcS2.b1', 'ignore_dqrs': ['D240126.7']},
        'ldis': {'dsname': 'ldS2.b1'},
        'mwr3c': {'dsname': 'mwr3cS2.b1'},
        'org': {'dsname': 'orgS2.b1'},
        'rain': {'dsname': 'raintbS2.b1'},
        'wsacr': {'dsname': 'wsacrcfrqcS2.b1'},

    }
}
