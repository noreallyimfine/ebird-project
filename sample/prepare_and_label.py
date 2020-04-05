import warnings
import pandas as pd
warnings.filterwarnings("ignore")

"""Clean and label subset of data for test modelling

Stesp include:
    - Read in 200K rows with 8 of the columns from bird csv
    - rename the columns
    - replace 'X' in 'Observation Count' with a 1
    - filter df for birds in the US
    - drop rows with NaN value in county - bad data
    - convert 'Observation Date' column to datetime object
    - extract month from date into its own columns
    - create 'season' column from month
    - combine 'county' and 'state' into single column for merge
    - load regions file
    - strip leading whitespace from 'State'
    - drop numbers attached to 'RegionName'
    - Map Alaska county names to match bird df
    - Capitalize 'city' in St. Louis and Richmond counties (hard-code)
    - drop 'parish' and 'county' from 'CountyName' to match merge
    - merge dataframes
    - create total rarity column
    - create regional rarity column
    - create seasonal regional rarity column"""

print("Reading in bird csv...")
print()
df = pd.read_csv('C:\\Users\\ajaco\\Downloads\\ebd_relJan-2020.txt',
                 sep='\t',
                 nrows=200000,
                 usecols=['COMMON NAME', 'COUNTRY', 'STATE', 'COUNTY',
                          'LATITUDE', 'LONGITUDE', 'OBSERVATION DATE',
                          'OBSERVATION COUNT'])

assert(df.shape == (200000, 8))

# ===============================

print("Renaming columns...")
print()
df.rename(columns={
    'COMMON NAME': 'name',
    'OBSERVATION COUNT': 'observ_count',
    'COUNTRY': 'country',
    'STATE': 'state',
    'COUNTY': 'county',
    'LATITUDE': 'latitude',
    'LONGITUDE': 'longitude',
    'OBSERVATION DATE': 'observ_date'
}, inplace=True)

assert('name' in df.columns)

# =================================

print("Filtering for birds seen in the United States...")
print()
us_birds = df.query("country == 'United States'")
assert(us_birds.shape == (105294, 8))
assert(len(us_birds['country'].unique()) == 1)

# ==================================

print("Dropping rows with null values for 'county' column")
print("These are bad data...")
print()
us_birds.dropna(subset=['county'], inplace=True)
assert(us_birds.isnull().sum()['county'] == 0)
assert(us_birds.shape == (105077, 8))

# ==================================

print("Dropping birds that are named poorly...")
print()

us_birds['bad_name'] = us_birds['name'].apply(lambda x: 0 if ("sp." in x) or ("(" in x) or ("/" in x) else 1)

mask = us_birds['bad_name'] == 0
us_birds = us_birds[~mask]

assert(us_birds.shape == (104333, 9))

# ==============================================

print("Dropping redundant column...")
print()

us_birds = us_birds.drop(columns=['bad_name'])
assert(us_birds.shape == (104333, 8))

# ==============================================
print('Replacing "X" in "Observation Count" with 1...')
print()
us_birds['observ_count'] = us_birds['observ_count'].apply(
                                    lambda x: 1 if x == 'X' else x)

assert('X' not in us_birds.observ_count.unique())

# ===================================

print("Converting 'Observation Date' to datetime object...")
print()
us_birds['observ_date'] = pd.to_datetime(us_birds['observ_date'], infer_datetime_format=True)
assert(us_birds.observ_date.dtype == 'datetime64[ns]')

# ===================================

print("Extracting month from 'Observation Date'...")
print()
us_birds['month'] = us_birds.observ_date.dt.month
assert('month' in us_birds.columns)
assert(us_birds.month.dtype == 'int64')

# ===================================

print("Creating a season column from the month column...")
print()


def season_from_month(x):
    if x in [12, 1, 2]:
        return 'Winter'
    elif x in [3, 4, 5]:
        return 'Spring'
    elif x in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'


us_birds['season'] = us_birds['month'].apply(season_from_month)
assert(us_birds.season.value_counts()['Spring'] == 39395)

# ======================================

print('Creating joint county and state column to merge on...')
print()
us_birds['county_state'] = us_birds['county'] + us_birds['state']
assert(us_birds.shape == (104333, 11))

# =======================================

print("Reading in file with regions on it...")
print()
regions = pd.read_excel("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\data\\URAmericaMapCountyList.xlsx",
                        skiprows=3,
                        usecols=['State', 'CountyName', 'RegionName'])

assert(regions.shape == (3142, 3))

# ======================================

print("Stripping leading whitespace from State...")
print()
regions['State'] = regions['State'].str.strip()
assert('California' in regions['State'].values)

# ======================================

print("Dropping leading numbers from RegionName...")
print()
regions['RegionName'] = regions['RegionName'].apply(lambda x: ' '.join(x.split()[1:]))
assert('Deep South' in regions['RegionName'].values)

# ======================================

print("Dropping state from CountyName...")
print()
regions['CountyName'] = regions['CountyName'].apply(lambda x: x.split(',')[0])
assert('Cook County' in regions['CountyName'].values)

# ======================================

print("Mapping names of Alaska counties to match the way...")
print("they're named in the bird df...")
print()
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

regions['CountyName'] = regions['CountyName'].apply(
    lambda x: county_dict[x] if x in county_dict.keys() else x
    )

assert('North Slope Borough' not in regions['CountyName'].values)

# ===============================================

print("Dropping 'Parish' from Louisiana counties...")
print()
regions['CountyName'] = regions['CountyName'].apply(lambda x: x if 'Parish' not in x else ' '.join(x.split()[:-1]))
assert('West Baton Rouge' in regions['CountyName'].values)

# ================================================

print("Capitalizing 'city' in Richmond and St. Louis county...")
print()
assert(regions.at[2944, 'CountyName'] == 'Richmond city')
assert(regions.at[1597, 'CountyName'] == 'St. Louis city')
regions.at[2944, 'CountyName'] = 'Richmond City'
regions.at[1597, 'CountyName'] = 'St. Louis City'

# ===============================================

print("Dropping 'county' from the counties that have it...")
print()
regions['CountyName'] = regions['CountyName'].apply(lambda x: x if 'County' not in x else ' '.join(x.split()[:-1]))
assert('Los Angeles' in regions['CountyName'].values)

# ===============================================

print('Creating joint county and state column to merge on...')
print()
regions['county_state'] = regions['CountyName'] + regions['State']
assert('AutaugaAlabama' in regions['county_state'].values)

# ===============================================

print("Merging birds and regions...")
print()
merged = us_birds.merge(regions)
assert(merged.shape == (103992, 14))

# ==============================================

print("Rarity label column for bird sightings by region and season...")
print()
season_region_ct = pd.pivot_table(merged,
                                  index='name',
                                  columns=['RegionName', 'season'],
                                  values='observ_count',
                                  aggfunc='count',
                                  fill_value=0.0)


def season_region_bird_rarity(bird, region, season):
    bird_percent = season_region_ct[(region, season)][bird] / season_region_ct[(region, season)].sum()
    if bird_percent > 0.005:
        return "Common"
    elif bird_percent > 0.001:
        return "Uncommon"
    else:
        return "Rare"


merged['seas_reg_rare'] = merged.apply(
    lambda x: season_region_bird_rarity(x['name'],
                                        x['RegionName'],
                                        x['season']), axis=1
    )

assert(merged.seas_reg_rare.value_counts(normalize=True)['Uncommon'] == 0.3044945765058851)

# ==============================================

print("Map rarity label to numeric...")
print()

label_dict = {"Common": 0, "Uncommon": 1, "Rare": 2}
merged['target'] = merged['seas_reg_rare'].map(label_dict)

assert(merged.shape == (103992, 16))
assert(merged['target'].value_counts()[0] == merged['seas_reg_rare'].value_counts()['Common'])

# ==============================================
print("Writing to csv...")
print()
merged.to_csv("labelled_bird_sample.csv", index=False)

# ===============================================

print("Data Cleaning and Preparation Complete.")
