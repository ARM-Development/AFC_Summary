# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'sgp',
    'facility': 'C1',
    'start_date': '2021-10-04',
    'end_date': '2021-10-15',
    'outname': '/home/theisen/www/afc_summary/sgp_tbs_tables.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'data_path': '/data/datastream',
    'info_style': 'simple',
    'dqr_table': False,
    'doi_table': False, #this will remove the DOI from besides the plots
    'instruments':{
        'cpc-air': {'dsname': 'tbscpcC1.b1'},
        'tbs': {'dsname': 'tbsgroundC1.b1'},
        'tbs-imet-a1': {'dsname': 'tbsimetC1.a1'},
        'tbs-imet': {'dsname': 'tbsimetC1.b1'},
        'tbs-imetxq2': {'dsname': 'tbsimetxq2C1.b1'},
        'pops-air': {'dsname': 'tbspopsC1.b1'},
        'tbs-wind-a1': {'dsname': 'tbswindC1.a1'},
        'tbs-wind': {'dsname': 'tbswindC1.b1'},
        'cpc-air-E36': {'dsname': 'tbscpcE36.b1'},
        'tbs-imet-a1-E36': {'dsname': 'tbsimetE36.a1'},
        'tbs-imet- E36': {'dsname': 'tbsimetE36.b1'},
        'tbs-imetxq2-E36': {'dsname': 'tbsimetxq2E36.b1'},
        'pops-air-E36': {'dsname': 'tbspopsE36.b1'},
        'tbs-wind-a1-E36': {'dsname': 'tbswindE36.a1'},
        'tbs-wind-E36': {'dsname': 'tbswindE36.b1'},
        'cpc-air-E9': {'dsname': 'tbscpcE9.b1'},
        'tbs-imet-a1-E9': {'dsname': 'tbsimetE9.a1'},
        'tbs-imet- E9': {'dsname': 'tbsimetE9.b1'},
        'tbs-imetxq2-E9': {'dsname': 'tbsimetxq2E9.b1'},
        'pops-air-E9': {'dsname': 'tbspopsE9.b1'},
        'tbs-wind-a1-E9': {'dsname': 'tbswindE9.a1'},
        'tbs-wind-E9': {'dsname': 'tbswindE9.b1'},
    }
}
