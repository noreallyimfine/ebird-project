'''
Using Pandas to process the entire bird file by using chunks and not reading 
it all into memory at once. Then write it to a new file.
'''

from helper import clean_regions, clean_bird_chunks

import pandas as pd

regions = pd.read_excel("..//Bird-Check/Back-End/URAmericaMapCountyList.xlsx",
                        skiprows=3,
                        usecols=['State', 'CountyName', 'RegionName'])


regions = clean_regions(regions)

bird_chunks = pd.read_csv("..//Bird-Check/bird_data.csv",
                          sep='\t',
                          chunksize=500000,
                          usecols=['COMMON NAME', 'COUNTRY', 'STATE', 'COUNTY',
                            'LATITUDE', 'LONGITUDE', 'OBSERVATION DATE',
                            'OBSERVATION COUNT'])
                          )