from joblib import load

# Path here is relative, may get messed up in future
encoder = load("bird_app/utils/cat_boost.joblib")
model = load("bird_app/utils/rf.joblib")

# Load birds, seasons, and regions
birds_list = load('bird_app/utils/birds_list.joblib')
seasons_list = load('bird_app/utils/seasons_list.joblib')
regions_list = load('bird_app/utils/regions_list.joblib')

# convert list to dict for displaying through flask template
# (Hoping this isn't necessary for displaying all the birds)
birds = [{'bird': bird} for bird in birds_list]
seasons = [{'season': season} for season in seasons_list]
regions = [{'region': region} for region in regions_list]

# TODO: load county_state list and parse to separate for form
# TODO: create dict to map countystate combo to region
county_state_list = load('bird_app/utils/county_state.joblib')
counties = [x.split(',')[0] for x in county_state_list]
states = [x.split(',')[1] for x in county_state_list]

# Load county-to-region mapping dict
cs_to_region = load('bird_app/utils/counties_to_regions.joblib')