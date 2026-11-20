# dsname: Datastream name to pull data from
# dsname2: Secondary datastream(s) to include and merge
# t_delta: Script will resample data to 1 min.  If gaps are longer set this appropriately
# workers: Set to 1 in the case of radar data so it doesn't crash the system
conf = {
    'site': 'bnf',
    'facility': 'M1',
    'start_date': '2025-04-01',
    'end_date': '2026-11-30',
    'outname': '/home/theisen/Code/AFC_Summary/images/bnf/bnf_dts_data_avail.pdf', #options are png, pdf, etc
    'chart_style': 'linear',
    'info_style': 'simple',
    'data_path': '/data/archive',
    'dqr_table': True,
    'doi_table': True, #this will remove the DOI from besides the plots
    'instruments':{
        'dts': {'dsname': 'bnftowerdtsch1S10.b1'},
        'dts2': {'dsname': 'bnftowerdtsch2S10.b1'},
        'dts3': {'dsname': 'bnftowerdtsch3S10.b1'},
        'dts4': {'dsname': 'bnftowerdtsch4S10.b1'},
    }
}
