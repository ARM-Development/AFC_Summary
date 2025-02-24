# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'crg',
    'facility': 'S3',
    'start_date': '2024-11-01',
    'end_date': '2025-11-30',
    'outname': '/home/theisen/Code/AFC_Summary/images/crg/crg_s3_data_availability.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'dl': {'dsname': 'dlfptS3.b1', 't_delta': 300},
        'ecor': {'dsname': 'ecorsfS3.b1', 't_delta': 30},
        'ldis': {'dsname': 'ldS3.b1'},
        'metwxt': {'dsname': 'metwxtS3.b1'},
        'mfrsr': {'dsname': 'mfrsr7nchS3.b1'},
        'mwr': {'dsname': 'mwrlosS3.b1'},
        'pops': {'dsname': 'popsS3.a1'},
        'sebs': {'dsname': 'sebsS3.b1', 't_delta': 30},
        'sirs': {'dsname': 'sirsS3.b1'},
    }
}
