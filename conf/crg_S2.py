# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'crg',
    'facility': 'S2',
    'start_date': '2024-11-01',
    'end_date': '2025-11-30',
    'outname': '/home/theisen/Code/AFC_Summary/images/crg/crg_s2_data_availability.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmS2.b1', 't_delta': 30},
        'aeth': {'dsname': 'aosaeth2spotS2.a1'},
        'aosmet': {'dsname': 'aosmetS2.a1'},
        'aps': {'dsname': 'aosapsS2.a1'},
        'ccn': {'dsname': 'aosccn2colaS2.b1'},
        'co-analyzer': {'dsname': 'aoscoS2.b1'},
        'cpc': {'dsname': 'aoscpcf1mS2.b1'},
        'cpc': {'dsname': 'aoscpcu1mS2.b1'},
        'htdma': {'dsname': 'aoshtdmaS2.a1', 't_delta': 60},
        'nephelometer': {'dsname': 'aosnephdry1mS2.b1'},
        'ozone': {'dsname': 'aoso3S2.b1'},
        'psap': {'dsname': 'aospsap3w1mS2.b1'},
        'smps': {'dsname': 'aossmpsS2.b1', 't_delta': 30},
        'so2': {'dsname': 'aosso2S2.b1'},
        'uhsas': {'dsname': 'aosuhsasS2.b1'},
        'ceil': {'dsname': 'ceilS2.b1'},
        'dl': {'dsname': 'dlfptS2.b1', 't_delta': 60},
        'ecor': {'dsname': 'ecorsfS2.b1', 't_delta': 30},
        'ldis': {'dsname': 'ldS2.b1'},
        'maws': {'dsname': 'mawsS2.b1'},
        'metwxt': {'dsname': 'metwxtS2.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchS2.b1'},
        'mwr3c': {'dsname': 'mwr3cS2.b1'},
        'pops': {'dsname': 'popsS2.a1'},
        'sebs': {'dsname': 'sebsS2.b1', 't_delta': 30},
        'sirs': {'dsname': 'sirsS2.b1'},
    }
}
