# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'epc',
    'facility': 'M1',
    'start_date': '2023-02-15',
    'end_date': '2023-04-14',
    'outname': '/home/theisen/Code/AFC_Summary/images/test.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'sp2': {'dsname': 'aossp2bc60sS2.b1'},
    }
}
