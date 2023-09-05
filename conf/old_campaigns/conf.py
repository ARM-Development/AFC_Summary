# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'anx',
    'facility': 'M1',
    'start_date': '2019-12-01',
    'end_date': '2020-05-31',
    'data_path': '/data/archive',
    'outname': '/home/theisen/www/afc_summary/test_conf.pdf',
    'chart_style': 'linear',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'metwxt': {'dsname': 'metwxtS2.b1'},
        'wb': {'dsname': 'wbpluvio2M1.a1'}
    }
}
