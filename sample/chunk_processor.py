'''
Using Pandas to process the entire bird file by using chunks and not reading 
it all into memory at once. Then writes it to a new file.
'''


# Master region cleaning function
def clean_regions(df):

    # Copy df
    df = df.copy()

    # rename columns
    df = region_column_renamer(df)

    # clean state, county, and region cols
    df = clean_cols(df)

    # fix county names
    df = county_fixed(df)

    # combine county state
    df = county_state_merger(df)

    return df

