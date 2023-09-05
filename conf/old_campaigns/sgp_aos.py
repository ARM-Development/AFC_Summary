# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'sgp',
    'facility': 'E13',
    'start_date': '2016-11-01',
    'end_date': '2022-03-01',
    'outname': '/home/theisen/www/afc_summary/sgp_aos_all.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmE13.b1', 't_delta': 30},
        'acsm-a0': {'dsname': 'aosacsmE13.a0', 't_delta': 30},
        'aps': {'dsname': 'aosapsE13.b1'},
        'aps-a1': {'dsname': 'aosapstofE13.a0'},
        'aosmet': {'dsname': 'aosmetE13.a1'},
        'caps-pmex': {'dsname': 'aoscaps3wE13.b1'},
        'caps-pmex-a1': {'dsname': 'aoscaps3wE13.a1'},
        'ccn': {'dsname': 'aosccn2colaE13.b1'},
        'ccn-a1': {'dsname': 'aosccn200E13.a1'},
        'cpc': {'dsname': 'aoscpcf1mE13.b1'},
        'cpc-a1': {'dsname': 'aoscpcfE13.a1'},
        'cpcuf': {'dsname': 'aoscpcuf1mE13.b1'},
        'cpcuf-a1': {'dsname': 'aoscpcufE13.a1'},
        'htdma': {'dsname': 'aoshtdmaE13.b1', 't_delta': 60},
        'htdma-a1': {'dsname': 'aoshtdmaE13.a1', 't_delta': 60},
        'nanosmps': {'dsname': 'aosnanosmpsE13.b1', 't_delta': 30},
        'nanosmps-a1': {'dsname': 'aosnanosmpsE13.a1', 't_delta': 30},
        'nephelometer-dry': {'dsname': 'aosnephdry1mE13.b1'},
        'nephelometer-dry-a1': {'dsname': 'aosnephdryE13.a1'},
        'nephelometer-wet': {'dsname': 'aosnephwet1mE13.b1'},
        'nephelometer-wet-a1': {'dsname': 'aosnephwetE13.a1'},
        'ozone': {'dsname': 'aoso3E13.b1'},
        'ozone-a1': {'dsname': 'aoso3E13.a1'},
        'psap': {'dsname': 'aospsap3w1mE13.b1'},
        'psap-a1': {'dsname': 'aospsap3wE13.a1'},
        'smps': {'dsname': 'aossmpsE13.b1', 't_delta': 30},
        'smps-a1': {'dsname': 'aossmpsE13.a1', 't_delta': 30},
        'so2': {'dsname': 'aosso2E13.b1'},
        'so2-a1': {'dsname': 'aosso2E13.a1'},
        'uhsas': {'dsname': 'aosuhsasE13.b1'},
        'uhsas-a1': {'dsname': 'aosuhsasE13.a1'},
    }
}
