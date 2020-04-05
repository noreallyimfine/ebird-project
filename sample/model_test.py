import pandas as pd
import joblib


# Get 50,000 new instances from dataset
df = pd.read_csv("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\data\\ebd_relJan-2020.txt", 
                  skiprows=200000,
                  nrows=50000,
                  usecols=['COMMON NAME', 'COUNTRY', 'STATE', 'COUNTY',
                           'LATITUDE', 'LONGITUDE', 'OBSERVATION DATE',
                           'OBSERVATION COUNT'])

assert(df.shape == (50000, 8))

