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

df = pd.read_csv('C:\\Users\\ajaco\\Downloads\\ebd_relJan-2020.txt',
				 sep='\t', 
				 nrows=200000, 
				 usecols=['COMMON NAME', 'COUNTRY', 'STATE', 'COUNTY', 'LATITUDE', 
				 		  'LONGITUDE', 'OBSERVATION DATE', 'OBSERVATION COUNT'])

assert(df.shape == (200000, 8))

#===============================

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

#=================================

us_birds = df.query("country == 'United States'")
assert(us_birds.shape == (105294, 8))
assert(len(us_birds['country'].unique() == 1))

#==================================

us_birds.dropna(subset=['county'], inplace=True)
assert(us_birds.isnull().sum()['county'] == 0)

#==================================

us_birds['observ_count'] = us_birds['observ_count'].apply(
									lambda x: 1 if x == 'X' else x)

assert('X' not in us_birds.observ_count.unique())

#===================================