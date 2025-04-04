# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'kcg',
    'facility': 'M1',
    'start_date': '2024-02-21',
    'end_date': '2025-06-14',
    'outname': '/home/theisen/Code/AFC_Summary/images/kcg/kcg_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        #'dl': {'dsname': 'dlfptM1.b1', 't_delta': 60, "workers": 1},
        'ecor': {'dsname': 'ecorsfM1.b1', 't_delta': 30},
        'irt': {'dsname': 'irtM1.b1'},
        'ldis': {'dsname': 'ldM1.b1'},
        'maws': {'dsname': 'mawsM1.b1'},
        'met': {'dsname': 'metM1.b1'},
        'mfr': {'dsname': 'mfr7nch10mM1.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        'mwr': {'dsname': 'mwrlosM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'rwp': {'dsname': '1290rwpwindconM1.a1', 't_delta': 60},
        'sebs': {'dsname': 'sebsM1.b1', 't_delta': 30},
        'sirs': {'dsname': 'sirsM1.b1'},
        'sonde': {'dsname': 'sondewnpnM1.b1', 't_delta': 1440./2},
        #'tsi': {'dsname': 'tsiskycoverM1.b1'},
        'vdis': {'dsname': 'vdisM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
        'aps': {'dsname': 'aosapsS3.b1'},
        'sp2': {'dsname': 'aossp2bc60sS3.b1'},
        'uhsas': {'dsname': 'aosuhsasS3.b1'},
        'aosmet': {'dsname': 'aosmetS2.a1'},
    }
}
