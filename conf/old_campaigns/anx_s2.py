# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'anx',
    'facility': 'S2',
    'start_date': '2019-12-01',
    'end_date': '2020-05-31',
    'outname': '/home/theisen/www/afc_summary/anx_s2.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'dqr_table': False,
    'doi_table': False, #this will remove the DOI from besides the plots
    'instruments':{
        'ceil': {'dsname': 'ceil10mS2.b1'},
        'dl': {'dsname': 'dlfptS2.b1', 'dsname2': 'dlppiS2.b1'},
        'ecor': {'dsname': '30ecorS2.b1', 't_delta': 30},
        'ldis': {'dsname': 'ldS2.b1'},
        'met': {'dsname': 'metwxtS2.b1'},
        'mpl': {'dsname': 'mplpolfsS2.b1'},
        'mwr': {'dsname': 'mwrlosS2.b1'},
        'tsi': {'dsname': 'tsiskycoverS2.b1'}
    }
}
