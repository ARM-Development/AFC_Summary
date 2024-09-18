# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'bnf',
    'facility': 'S40',
    'start_date': '2024-9-01',
    'end_date': '2025-10-01',
    'outname': '/home/theisen/Code/AFC_Summary/images/bnf/bnf_S40_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeriS40': {'dsname': 'aerisummaryS40.b1'},
        'dlS40': {'dsname': 'dlfptS40.b1', 't_delta': 60},
        'mwr3cS40': {'dsname': 'mwr3cS40.b1'},
        'ecorS40': {'dsname': '30ecorS40.b1', 't_delta': 30},
        'gndradS40': {'dsname': 'gndrad60sS40.b1'},
        'irtS40': {'dsname': 'irtS40.b1'},
        'metS40': {'dsname': 'metS40.b1'},
        'mfrsrS40': {'dsname': 'mfrsr7nchS40.b1'},
        'sebsS40': {'dsname': 'sebsS40.b1'},
        'skyradS40': {'dsname': 'skyrad60sS40.b1'},
        'stampS40': {'dsname': 'stampS40.b1'},
    }
}
