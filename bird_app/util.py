from joblib import load

# Path here is relative, may get messed up in future
# encoder = load("bird_app/utils/cat_boost.joblib")
# model = load("bird_app/utils/rf.joblib")

# Load birds, seasons, and regions
regions = load('bird_app/utils/regions_list.joblib')

# convert list to dict for displaying through flask template
# (Hoping this isn't necessary for displaying all the birds)
birds = load('bird_app/utils/birds_list.joblib')
seasons = load('bird_app/utils/seasons_list.joblib')
regions = load('bird_app/utils/regions_list.joblib')

# TODO: load county_state list and parse to separate for form
# TODO: create dict to map countystate combo to region
county_states = load('bird_app/utils/county_state.joblib')
states = [cs.split(',')[1] for cs in county_states]
counties = [cs.split(',')[0] for cs in county_states]

# Load county-to-region mapping dict
cs_to_region = load('bird_app/utils/counties_to_regions.joblib')
