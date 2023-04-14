# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'epc',
    'facility': 'M1',
    'start_date': '2023-02-15',
    'end_date': '2024-02-14',
    'outname': '/home/theisen/Code/AFC_Summary/images/epc_aos_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmM1.b1', 't_delta': 30},
        'aeth': {'dsname': 'aosaeth2spotM1.a1'},
        'aosmet': {'dsname': 'aosmetM1.a1'},
        'ccn': {'dsname': 'aosccn2colaM1.b1'},
        'co-analyzer': {'dsname': 'aoscoM1.b1'},
        'cpc': {'dsname': 'aoscpcf1mM1.b1'},
        'cpc': {'dsname': 'aoscpcu1mM1.b1'},
        'htdma': {'dsname': 'aoshtdmaM1.a1', 't_delta': 11},
        'nephelometer': {'dsname': 'aosnephdry1mM1.b1'},
        'nephelometer': {'dsname': 'aosnephwet1mM1.b1'},
        'ozone': {'dsname': 'aoso3M1.b1'},
        'psap': {'dsname': 'aospsap3w1mM1.b1'},
        'smps': {'dsname': 'aossmpsM1.b1', 't_delta': 30},
        'so2': {'dsname': 'aosso2M1.b1'},
        'uhsas': {'dsname': 'aosuhsasM1.b1'},
    }
}
