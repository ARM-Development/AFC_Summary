# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'epc',
    'facility': 'M1',
    'start_date': '2023-02-15',
    'end_date': '2024-02-14',
    'outname': '/home/theisen/Code/AFC_Summary/images/epc_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        'dl': {'dsname': 'dlfptM1.b1'},
        'ecor': {'dsname': '30ecorM1.b1', 't_delta': 30},
        'gndrad': {'dsname': 'gndrad60sM1.b1'},
        'irt': {'dsname': 'irtsstM1.b1'},
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
        'rwp': {'dsname': '1290bsrwpwindavgM1.b1', 't_delta': 60},
        'sashe': {'dsname': 'sashemfrM1.b1'},
        'sasze': {'dsname': 'saszefilterbandsM1.a1'},
        'sebs': {'dsname': 'sebsM1.b1', 't_delta': 30},
        'skyrad': {'dsname': 'skyrad60sM1.b1'},
        'sonde': {'dsname': 'sondewnpnM1.b1', 't_delta': 1440./4.},
        'tsi': {'dsname': 'tsiskycoverM1.b1'},
        'vdis': {'dsname': 'vdisM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
        'ceilS2': {'dsname': 'ceilS2.b1'},
        'dlS2': {'dsname': 'dlfptS2.b1'},
        'ldisS2': {'dsname': 'ldS2.b1'},
        'mwr3cS2': {'dsname': 'mwr3cS2.b1'},
        'orgS2': {'dsname': 'orgS2.b1'},
        'rainS2': {'dsname': 'raintbS2.b1'},

    }
}
