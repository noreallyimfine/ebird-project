import pandas as pd

df = pd.read_csv("data\\us_birds.csv")
print(df.shape)

# season_region_ct = pd.pivot_table(df,
#                                   index='common_name',
#                                   columns=['region', 'season'],
#                                   values='observ_count',
#                                   aggfunc='count',
#                                   fill_value=0.0)

# print(season_region_ct)