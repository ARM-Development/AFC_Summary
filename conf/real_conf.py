# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'sgp',
    'facility': 'C1',
    'start_date': '2025-12-01',
    'end_date': '2026-09-15',
    'outname': '/home/theisen/Code/AFC_Summary/images/sgp/REAL_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    # Processing and data paths
    'cache_dir': '~/.cache/afc_summary',
    'data_path': '/data/archive',
    'instruments':{
        'ceil': {'dsname': 'ceilC1.b1'},
        'ceilpol': {'dsname': 'ceilpolC1.b1'},
        'dl': {'dsname': 'dlfptC1.b1', 't_delta': 60, 'workers': 1},
        'hsrl': {'dsname': 'hsrlC1.a1'},
        'mpl': {'dsname': 'mplpolfsC1.b1'},
        'mpl': {'dsname': 'minimplC1.b1'},
        'rl': {'dsname': 'rlC1.a0', 't_delta': 5},
    }
}
