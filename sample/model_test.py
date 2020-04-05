import pandas as pd
import joblib


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

# Drop columns where county is missing
print(us_birds.isnull().sum()['county'])