import pandas as pd
import joblib

from sklearn.metrics import accuracy_score


# Get 50,000 new instances from dataset
df = pd.read_csv("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\data\\ebd_relJan-2020.txt",
                 sep='\t',
                 skiprows=lambda x: x in range(1, 200001),
                 nrows=50000,
                 usecols=['COMMON NAME', 'COUNTRY', 'STATE', 'COUNTY',
                          'LATITUDE', 'LONGITUDE', 'OBSERVATION DATE',
                          'OBSERVATION COUNT'])

assert(df.shape == (50000, 8))


# Renaming columns
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


# Slice to just birds in the U.S.
us_birds = df.query("country == 'United States'")
assert(us_birds.shape == (28548, 8))
assert(len(us_birds['country'].unique()) == 1)

# Copying dataframe
us_birds = us_birds.copy()

# Drop columns where county is missing
assert(us_birds.isnull().sum()['county'] == 0)

# Check for birds with names that we dropped for training
us_birds['bad_name'] = us_birds['name'].apply(lambda x: 0 if ("sp." in x) or ("(" in x) or ("/" in x) else 1)

mask = us_birds['bad_name'] == 0
us_birds = us_birds[~mask].drop(columns=['bad_name'])
assert(us_birds.shape == (28373, 8))

# Extract month for season
us_birds['observ_date'] = pd.to_datetime(us_birds['observ_date'], infer_datetime_format=True)
us_birds['month'] = us_birds.observ_date.dt.month


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

# Merge column
us_birds['county_state'] = us_birds['county'] + us_birds['state']


# Read in regions file
regions = pd.read_excel("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\data\\URAmericaMapCountyList.xlsx",
                        skiprows=3,
                        usecols=['State', 'CountyName', 'RegionName'])


regions['State'] = regions['State'].str.strip()
regions['RegionName'] = regions['RegionName'].apply(lambda x: ' '.join(x.split()[1:]))
regions['CountyName'] = regions['CountyName'].apply(lambda x: x.split(',')[0])

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

regions['CountyName'] = regions['CountyName'].apply(lambda x: x if 'Parish' not in x else ' '.join(x.split()[:-1]))
regions.at[2944, 'CountyName'] = 'Richmond City'
regions.at[1597, 'CountyName'] = 'St. Louis City'

regions['CountyName'] = regions['CountyName'].apply(lambda x: x if 'County' not in x else ' '.join(x.split()[:-1]))

regions['county_state'] = regions['CountyName'] + regions['State']

# Merge dataframes
merged = us_birds.merge(regions)
print(merged.shape)

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

# Numeric label
label_dict = {"Common": 0, "Uncommon": 1, "Rare": 2}
merged['target'] = merged['seas_reg_rare'].map(label_dict)

# Run through model
model = joblib.load("rf.joblib")
encoder = joblib.load("cat_boost.joblib")

features = ['name', 'season', 'RegionName']
target = 'target'

X = merged[features]
y = merged[target]

X = encoder.transform(X)

preds = model.predict(X)

print("\n\n")
print("=====================\n")
print(f"    {accuracy_score(y, preds)}    ")
print("=====================\n")
print("\n\n")
