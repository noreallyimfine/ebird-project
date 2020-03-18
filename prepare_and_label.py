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
assert(us_birds.shape == (105077, 8))
#==================================

us_birds['observ_count'] = us_birds['observ_count'].apply(
									lambda x: 1 if x == 'X' else x)

assert('X' not in us_birds.observ_count.unique())

#===================================

us_birds['observ_date'] = pd.to_datetime(us_birds['observ_date'], infer_datetime_format=True)
assert(us_birds.observ_date.dtype == 'datetime64[ns]')

#===================================

us_birds['month'] = us_birds.observ_date.dt.month
assert('month' in us_birds.columns)
assert(us_birds.month.dtype == 'int64')

#===================================

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
assert(us_birds.season.value_counts()['Spring'] == 39610)

#======================================

us_birds['county_state'] = us_birds['county'] + us_birds['state']
assert(us_birds.shape == (105077, 11))

#=======================================

regions = pd.read_excel("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\URAmericaMapCountyList.xlsx",
						skiprows=3,
						usecols=['State', 'CountyName', 'RegionName'])

assert(regions.shape == (3142, 3))

#======================================

regions['State'] = regions['State'].str.strip()

assert('California' in regions['State'].values)

#======================================

regions['RegionName'] = regions['RegionName'].apply(lambda x: ' '.join(x.split()[1:]))
assert('Deep South' in regions['RegionName'].values)

#======================================

regions['CountyName'] = regions['CountyName'].apply(lambda x: x.split(',')[0])
assert('Cook County' in regions['CountyName'].values)

#======================================

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

#===============================================

