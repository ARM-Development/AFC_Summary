# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'hou',
    'facility': 'M1',
    'outname': '/home/theisen/www/afc_summary/hou_tables_prev_7_days.pdf', #options are png, pdf, etc
    'previous_days': 7,
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/datastream',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        'dl': {'dsname': 'dlfptM1.b1'},
        'ecor': {'dsname': '30ecorM1.b1', 't_delta': 30},
        'gndrad': {'dsname': 'gndrad60sM1.b1'},
        'gndirt': {'dsname': 'gndirtM1.b1'},
        'irt': {'dsname': 'irtM1.b1'},
        #'kazr': {'dsname': 'kazrcfrgeM1.a1', 'workers': 1, 'data_path': '/data/datastream'},
        #'kasacr': {'dsname': 'kasacrcfrM1.a1', 'workers': 1, 'data_path': '/data/datastream'},
        'ldis': {'dsname': 'ldM1.b1'},
        'maws': {'dsname': 'mawsM1.b1'},
        'met': {'dsname': 'metM1.b1'},
        'mfr': {'dsname': 'mfr7nch10mM1.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        'mwr': {'dsname': 'mwrlosM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'mwrhf': {'dsname': 'mwrhfM1.b1'},
        'nfov': {'dsname': 'nfov2chM1.b1'},
        'rwp': {'dsname': '915rwpwindconX10.a1', 'dsname2': '915rwpprecipconX10.a1', 't_delta': 60},
        '1290rwp': {'dsname': '1290rwpwindconM1.a1', 'dsname2': '1290rwpprecipconM1.a1', 't_delta': 60},
        'sebs': {'dsname': 'sebsM1.b1', 't_delta': 30},
        'skyrad': {'dsname': 'skyrad60sM1.b1'},
        'tsi': {'dsname': 'tsiskycoverM1.b1'},
        'vdis': {'dsname': 'vdisM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
        'ldis-S3': {'dsname': 'ldS3.b1'},
        'maws-S3': {'dsname': 'mawsS3.b1'},
        'met-S3': {'dsname': 'metS3.b1'},
        'mwr-S3': {'dsname': 'mwrlosS3.b1'},
        'sonde-S3': {'dsname': 'sondewnpnS3.b1'},
        #'xsacr': {'dsname': 'xsacrcfrM1.a1', 'workers': 1, 'data_path': '/data/datastream'},
    }
}
