# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'crg',
    'facility': 'M1',
    'start_date': '2024-12-01',
    'end_date': '2025-11-30',
    'outname': '/home/theisen/Code/AFC_Summary/images/crg/crg_M1_data_availability.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        'dl': {'dsname': 'dlfptM1.b1', 't_delta': 300},
        'gndirt': {'dsname': 'gndirtM1.b1'},
        'irt': {'dsname': 'irtM1.b1'},
        'ldis': {'dsname': 'ldM1.b1'},
        'maws': {'dsname': 'mawsM1.b1'},
        'met': {'dsname': 'metM1.b1'},
        'mfr': {'dsname': 'mfr7nch10mM1.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'nfov': {'dsname': 'nfov2chM1.b1'},
        'pops': {'dsname': 'popsM1.a1'},
        'rwp': {'dsname': '915rwpprecipmeanhighM1.a1', 'dsname2': 'crg915rwpprecipmomM1.a0', 't_delta': 10},
        'sirs': {'dsname': 'sirsM1.b1'},
        'vdis': {'dsname': 'vdisM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
    }
}
