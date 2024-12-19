# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'bnf',
    'facility': 'M1',
    'start_date': '2024-9-01',
    'end_date': '2025-10-01',
    'outname': '/home/theisen/Code/AFC_Summary/images/bnf/bnf_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmtofspecM1.a1', 't_delta': 10},
        'aosmet': {'dsname': 'aosmetM1.a1'},
        'aps': {'dsname': 'aosapsM1.b1'},
        'caps': {'dsname': 'aoscaps3wM1.b1'},
        'ccn': {'dsname': 'aosccn2colaM1.b1'},
        'co-analyzer': {'dsname': 'aoscoM1.b1'},
        'cpc': {'dsname': 'aoscpcf1mM1.b1'},
        'cpc': {'dsname': 'aoscpcu1mM1.b1'},
        'htdma': {'dsname': 'aoshtdmaM1.a1', 't_delta': 60},
        'nephelometer': {'dsname': 'aosnephdry1mM1.b1'},
        'ozone': {'dsname': 'aoso3M1.b1'},
        'psap': {'dsname': 'aospsap3w1mM1.b1'},
        'smps': {'dsname': 'aossmpsM1.b1', 't_delta': 30},
        'so2': {'dsname': 'aosso2M1.b1'},
        'uhsas': {'dsname': 'aosuhsasM1.b1'},
        'aeri': {'dsname': 'aerisummaryM1.b1'},
        'asi': {'dsname': 'asiskycoverM1.b1'},
        'ceil': {'dsname': 'ceilM1.b1'},
        'dl': {'dsname': 'dlfptM1.b1', 't_delta': 60, 'workers': 1},
        'gndrad': {'dsname': 'gndrad60sM1.b1'},
        'hsrl': {'dsname': 'hsrlM1.a1'},
        'irt': {'dsname': 'irtM1.b1'},
        'ldis': {'dsname': 'ldM1.b1'},
        'maws': {'dsname': 'mawsM1.b1'},
        'met': {'dsname': 'metM1.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchM1.b1'},
        'mpl': {'dsname': 'mplpolfsM1.b1'},
        'mwr3c': {'dsname': 'mwr3cM1.b1'},
        'rl': {'dsname': 'rlM1.a0'},
        'rwp': {'dsname': '915rwpprecipavghiresM1.a1', 't_delta': 10},
        'skyrad': {'dsname': 'skyrad60sM1.b1'},
        'sonde': {'dsname': 'sondewnpnM1.b1', 't_delta': 1440./3},
        'vdis': {'dsname': 'vdisM1.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'},
    }
}
