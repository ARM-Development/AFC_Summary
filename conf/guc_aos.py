# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'guc',
    'facility': 'S2',
    'start_date': '2021-09-01',
    'end_date': '2023-06-15',
    'outname': '/home/theisen/Code/AFC_Summary/images/guc_aos_summary.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'aosacsmtofspecS2.a1', 't_delta': 30},
        'ccn': {'dsname': 'aosccn2colaS2.b1'},
        'co-analyzer': {'dsname': 'aoscoS2.b1'},
        'cpc': {'dsname': 'aoscpcf1mS2.b1'},
        'cpcuf': {'dsname': 'aoscpcuf1mS2.b1'},
        'htdma': {'dsname': 'aoshtdmaS2.a1', 't_delta': 60},
        'aosmet': {'dsname': 'aosmetS2.a1'},
        'nephelometer': {'dsname': 'aosnephdry1mS2.b1'},
        'ozone': {'dsname': 'aoso3S2.a1'},
        'psap': {'dsname': 'aospsap3w1mS2.b1'},
        'smps': {'dsname': 'aossmpsS2.a1', 't_delta': 30},
        'sp2': {'dsname': 'aossp2bc60sS2.b1'},
        'uhsas': {'dsname': 'aosuhsasS2.b1'},
    }
}
