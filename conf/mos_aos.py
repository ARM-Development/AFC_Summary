# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'mos',
    'facility': 'M1',
    'start_date': '2019-10-01',
    'end_date': '2020-10-01',
    'outname': '/home/theisen/www/afc_summary/mos_aos_tables.pdf',
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aosmet': {'dsname': 'aosmetM1.a1'},
        'ccn': {'dsname': 'aosccn2colaM1.b1'},
        'ccn-a1': {'dsname': 'aosccn200M1.a1'},
        'co-analyzer': {'dsname': 'aoscoM1.b1'},
        'co-analyzer-a1': {'dsname': 'aoscoM1.a1'},
        'cpc': {'dsname': 'aoscpcf1mM1.b1'},
        'cpc-a1': {'dsname': 'aoscpcfM1.a1'},
        'cpcuf': {'dsname': 'aoscpcuf1mM1.b1'},
        'cpcuf-a1': {'dsname': 'aoscpcufM1.a1'},
        'htdma': {'dsname': 'aoshtdmaM1.b1', 't_delta': 60},
        'htdma-a1': {'dsname': 'aoshtdmaM1.a1', 't_delta': 60},
        'aos': {'dsname': 'aosimpactorM1.a1'},
        'nephelometer-dry': {'dsname': 'aosnephdry1mM1.b1'},
        'nephelometer-dry-a1': {'dsname': 'aosnephdryM1.a1'},
        'ozone': {'dsname': 'aoso3M1.b1'},
        'ozone-a1': {'dsname': 'aoso3M1.a1'},
        'psap': {'dsname': 'aospsap3w1mM1.b1'},
        'psap-a1': {'dsname': 'aospsap3wM1.a1'},
        'smps': {'dsname': 'aossmpsM1.b1', 't_delta': 30},
        'smps-a1': {'dsname': 'aossmpsM1.a1', 't_delta': 30},
        'sp2': {'dsname': 'aossp2bc60sM1.c1'},
        'uhsas': {'dsname': 'aosuhsasM1.b1'},
        'uhsas-a1': {'dsname': 'aosuhsasM1.a1'},
    }
}
