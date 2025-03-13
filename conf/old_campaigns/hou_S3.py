# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'hou',
    'facility': 'S3',
    'start_date': '2022-05-01',
    'end_date': '2022-10-01',
    'outname': '/home/theisen/Code/AFC_Summary/images/hou/hou_S3_data_availability.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'acsm': {'dsname': 'acsmtofcdceS3.c1', 't_delta': 30},
        'aosmet': {'dsname': 'aosmetS3.a1'},
        'opc': {'dsname': 'aosopcS3.b1'},
        'ceil': {'dsname': 'ceilpblhtS3.a0'},
        'ldis': {'dsname': 'ldS3.b1'},
        'maws': {'dsname': 'mawsS3.b1'},
        'met': {'dsname': 'metS3.b1'},
        'mwr': {'dsname': 'mwrlosS3.b1'},
        'mwr3c': {'dsname': 'mwr3cS3.b1'},
    }
}
