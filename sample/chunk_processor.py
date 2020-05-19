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
    
    # Map Alaska counties
    county_dict = {
        'Aleutians East Borough': 'Aleutians East',
        'Aleutians West Census Area': 'Aleutians West',
        'Anchorage Municipality': 'Anchorage',
        'Bethel Census Area': 'Bethel',
        'Bristol Bay Borough': 'Bristol Bay',
        'Denali Borough': 'Denali',
        'Dillingham Census Area': 'Dillingham',
        'Fairbanks North Star Borough': 'Fairbanks North Star',
        'Haines Borough': 'Haines',
        'Hoonah-Angoon Census Area': 'Skagway-Hoonah-Angoon',
        'Juneau City and Borough': 'Juneau',
        'Kenai Peninsula Borough': 'Kenai Peninsula',
        'Ketchikan Gateway Borough': 'Ketchikan Gateway',
        'Kodiak Island Borough': 'Kodiak Island',
        'Kusilvak Census Area': 'Kusilvak',
        'Lake and Peninsula Borough': 'Lake and Peninsula',
        'Matanuska-Susitna Borough': 'Matanuska-Susitna',
        'Nome Census Area': 'Nome',
        'North Slope Borough': 'North Slope',
        'Northwest Arctic Borough': 'Northwest Arctic',
        'Petersburg Borough': 'Petersburg Borough',
        'Prince of Wales-Hyder Census Area': 'Prince of Wales-Outer Ketchikan',
        'Sitka City and Borough': 'Sitka',
        'Southeast Fairbanks Census Area': 'Southeast Fairbanks',
        'Valdez-Cordova Census Area': 'Valdez-Cordova',
        'Yakutat City and Borough': 'Yakutat',
        'Yukon-Koyukuk Census Area': 'Yukon-Koyukuk'
    }

    df['county'] = df['county'].apply(
        lambda x: county_dict[x] if x in county_dict.keys() else x
    )

    # drop parish from county col
    df['county'] = df['county'].apply(
        lambda x: x if 'Parish' not in x else ' '.join(x.split()[:-1])
    )

    # drop county from county col
    df['county'] = df['county'].apply(
        lambda x: x if 'County' not in x else ' '.join(x.split()[:-1])
    )


def bird_column_renamer(df):
    return df.rename(columns={
        'COMMON NAME': 'name',
        'OBSERVATION DATE': 'observ_date',
        'COUNTRY': 'country',
        'STATE': 'state',
        'COUNTY': 'county'
    })

def us_bird_filter(df):
    return df.query("country == 'United States'")

def bad_name_cleaner(df):
    df['bad_name'] = df['name'].apply(
        lambda x: 0 if ("sp." in x) or ("(" in x) or ("/" in x) else 1
    )
    mask = (df['bad_name'] == 0)
    df = df[~mask].drop(columns=['bad_name'])

def get_season(df):
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
