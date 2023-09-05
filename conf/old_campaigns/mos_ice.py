# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'mos',
    'facility': 'M1',
    'start_date': '2019-10-01',
    'end_date': '2020-9-30',
    'outname': '/home/theisen/www/afc_summary/mos_s3_tables.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'irt': {'dsname': 'irtS3.b1'},
        'gndirt': {'dsname': 'gndirtS3.b1'},
        'gndrad': {'dsname': 'gndrad60sS3.b1'},
        'ldis': {'dsname': 'ldS3.b1'},
        'mfr': {'dsname': 'mfr3mS3.b1'},
        'met': {'dsname': 'pwdS3.b1'},
        'wb': {'dsname': 'wbpluvio2S3.a1'}
    }
}
