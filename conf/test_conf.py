# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'hou',
    'facility': 'M1',
    'start_date': '2021-10-01',
    'end_date': '2022-10-01',
    'outname': '/home/theisen/www/afc_summary/hou_tables_linear.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'rwp': {'dsname': '915rwpwindconX10.a1', 'dsname2': '915rwpprecipconX10.a1', 't_delta': 60, 'num_workers': 1},
    }
}
