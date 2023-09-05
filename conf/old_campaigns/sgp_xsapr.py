# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'sgp',
    'facility': 'I4',
    'start_date': '2011-04-01',
    'end_date': '2022-12-31',
    'outname': '/home/theisen/www/afc_summary/sgp_xsapr.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/dq_qme',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'xsapr': {'dsname': 'xsaprrawI4.00'},
        'xsapr': {'dsname': 'xsaprrawI5.00'},
        'xsapr': {'dsname': 'xsaprrawI6.00'},
    }
}
