# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'bnf',
    'facility': 'S30',
    'start_date': '2024-9-01',
    'end_date': '2025-10-01',
    'outname': '/home/theisen/Code/AFC_Summary/images/bnf/bnf_S30_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeriSi30': {'dsname': 'aerisummaryS30.b1'},
        'mwr3cS30': {'dsname': 'mwr3cS30.b1'},
        'ecorS30': {'dsname': '30ecorS30.b1', 't_delta': 30},
        'gndradS30': {'dsname': 'gndrad60sS30.b1'},
        'irtS30': {'dsname': 'irtS30.b1'},
        'metS30': {'dsname': 'metS30.b1'},
        'mfrsrS30': {'dsname': 'mfrsr7nchS30.b1'},
        'sebsS30': {'dsname': 'sebsS30.b1'},
        'skyradS30': {'dsname': 'skyrad60sS30.b1'},
        'stampS30': {'dsname': 'stampS30.b1'},
    }
}
