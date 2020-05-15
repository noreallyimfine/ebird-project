'''
Using Pandas to process the entire bird file by using chunks and not reading 
it all into memory at once. Then writes it to a new file.
'''

def region_column_renamer(df):
    return df.rename(columns={
        'State': 'state',
        'CountyName': 'county',
        'RegionName': 'region'
    })

def clean_cols(df):

    # Strip leading whitespace
    df['state'] = df['state'].str.strip()

    # drop number from region
    df['region'] = df['region'].apply(lambda x: ' '.join(x.split()[1:]))

    # drop state from county
    df['county'] = df['county'].apply(lambda x: x.split(',')[0])

def county_fixer(df):
    pass

# Master region cleaning function
def clean_regions(df):

    # Copy df
    df = df.copy()

    # rename columns
    df = region_column_renamer(df)

    # clean state, county, and region cols
    df = clean_cols(df)

    # fix county names
    df = county_fixer(df)

    # combine county state
    df = county_state_merger(df)

    return df

# Master bird chunk cleaner
def clean_bird_chunks(df):

    # copy df
    df = df.copy()

    # rename columns
    df = bird_column_renamer(df)

    # filter for us birds
    df = us_bird_filter(df)

    # drop nulls
    df = df.dropna(subset=['county'])

    # clean badly named birds
    df = bad_name_cleaner(df)

    # get season thru date
    df = get_season(df)

    # combine county state
    df = county_state_merger(df)

    return df 
