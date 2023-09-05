# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'mos',
    'facility': 'M1',
    'start_date': '2019-10-01',
    'end_date': '2020-10-01',
    'outname': '/home/theisen/Code/AFC_Summary/images/mos_M1_summary.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1', 't_delta': 5},
        'ceil': {'dsname': 'ceilM1.b1'},
        'dl': {'dsname': 'dlfptM1.a1'},
        'hsrl': {'dsname': 'hsrlM1.a1'},
        #'kazr': {'dsname': 'kazrcfrgeM1.a1', 'workers': 1},
        'ldis': {'dsname': 'ldM1.b1'},
        'met': {'dsname': 'pwdM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        #'mwacr': {'dsname': 'mwacrcfrM1.a1', 'workers': 1},
        'mwr': {'dsname': 'mwrlosM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'rwp': {'dsname': '1290bsrwpwindavgM1.b1', 't_delta': 60},
        'rain': {'dsname': 'srgM1.a1'},
        'sonde': {'dsname': 'sondewnpnM1.b1', 't_delta': 1440/2},
        'tsi': {'dsname': 'tsiskycoverM1.b1'}
    }
}
