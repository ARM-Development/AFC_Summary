# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'guc',
    'facility': 'M1',
    'start_date': '2021-09-01',
    'end_date': '2023-06-15',
    'outname': '/home/theisen/Code/AFC_Summary/images/guc_M1_summary.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        #'dl': {'dsname': 'dlfptM1.b1', 'dsname2': 'dlppiM1.b1'},
        'ecor': {'dsname': '30ecorM1.b1', 't_delta': 30},
        'gndrad': {'dsname': 'gndrad60sM1.b1'},
        'gndirt': {'dsname': 'gndirtM1.b1'},
        'hsrl': {'dsname': 'hsrlM1.a1'},
        'irt': {'dsname': 'irtM1.b1'},
        #'kazr': {'dsname': 'kazrcfrgeM1.a1', 'workers': 1},
        'ldis': {'dsname': 'ldM1.b1'},
        'maws': {'dsname': 'mawsM1.b1'},
        'met': {'dsname': 'metM1.b1'},
        'mfr': {'dsname': 'mfr7nch10mM1.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        'mwr': {'dsname': 'mwrlosM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'rwp': {'dsname': '915rwpwindmeanlowM1.a1', 'dsname2': '915rwpprecipmeanlowM1.a1', 't_delta': 60},
        'sebs': {'dsname': 'sebsM1.b1', 't_delta': 30},
        'skyrad': {'dsname': 'skyrad60sM1.b1'},
        'sonde': {'dsname': 'sondewnpnM1.b1', 't_delta': 1440/2},
        'tsi': {'dsname': 'tsiskycoverM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
    }
}
