"""Testing the joblib files of the choices for the front-end"""

import joblib

birds = joblib.load("sample/birds_list.joblib")
season = joblib.load("sample/seasons_list.joblib")
regions = joblib.load("sample/regions_list.joblib")

print("Birds:", birds)
print("\n\n")
print("Seasons:", season)
print("\n\n")
print("Regions:", regions)
