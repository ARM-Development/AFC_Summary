# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'guc',
    'facility': 'M1',
    'start_date': '2021-09-01',
    'end_date': '2023-06-15',
    'outname': '/home/theisen/Code/AFC_Summary/images/guc_dl_test.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'dl': {'dsname': 'dlfptM1.b1', 'dsname2': 'dlppiM1.b1'},
    }
}
