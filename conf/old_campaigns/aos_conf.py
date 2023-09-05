# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'anx',
    'facility': 'M1',
    'start_date': '2019-12-01',
    'end_date': '2020-05-31',
    'outname': '/home/theisen/www/afc_summary/anx_aos_table.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmM1.b1', 't_delta': 30},
        'aeth': {'dsname': 'aosaeth2spotM1.a1'},
        'ccn': {'dsname': 'aosccn2colaM1.b1'},
        'co-analyzer': {'dsname': 'aoscoM1.b1'},
        'cpc': {'dsname': 'aoscpcf1mM1.b1'},
        'cpc': {'dsname': 'aoscpcu1mM1.b1'},
        'htdma': {'dsname': 'aoshtdmaM1.a1', 't_delta': 60},
        'aosmet': {'dsname': 'aosmetM1.a1'},
        'nephelometer': {'dsname': 'aosnephdry1mM1.b1'},
        'nephelometer': {'dsname': 'aosnephwet1mM1.b1'},
        'ozone': {'dsname': 'aoso3M1.b1'},
        'psap': {'dsname': 'aospsap3w1mM1.b1'},
        'smps': {'dsname': 'aossmpsM1.a1', 't_delta': 30},
        'uhsas': {'dsname': 'aosuhsasM1.b1'}
    }
}
