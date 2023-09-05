# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'mos',
    'facility': 'M1',
    'start_date': '2019-10-01',
    'end_date': '2020-10-01',
    'outname': '/home/theisen/www/afc_summary/mos_aos_tables_a1.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'aosmet': {'dsname': 'aosmetM1.a1', 't_delta': 60},
        'ccn': {'dsname': 'aosccn200M1.a1'},
        'co-analyzer': {'dsname': 'aoscoM1.a1'},
        'cpc': {'dsname': 'aoscpcfM1.a1'},
        'cpcuf': {'dsname': 'aoscpcufM1.a1'},
        'htdma': {'dsname': 'aoshtdmaM1.a1', 't_delta': 60},
        'aos': {'dsname': 'aosimpactorM1.a1', 't_delta': 60},
        'nephelometer': {'dsname': 'aosnephdryM1.a1'},
        'ozone': {'dsname': 'aoso3M1.a1'}, #Bad times!
        'psap': {'dsname': 'aospsap3wM1.a1'},
        'smps': {'dsname': 'aossmpsM1.a1', 't_delta': 30},
        #'sp2': {'dsname': 'aossp2auxM1.a0'},
        'uhsas': {'dsname': 'aosuhsasM1.a1'},
    }
}
