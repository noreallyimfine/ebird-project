from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import category_encoders as ce
import pandas as pd
import numpy as np

# ======================================

print("Reading in labeled dataset sample...")
print()

df = pd.read_csv("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\labelled_bird_sample.csv")
assert(df.shape == (103992, 16))

# ========================================

print("Select features and target to split dataframe into X and y...")
print()

features = ['name', 'season', 'RegionName', 'latitude', 'longitude']
target = 'target'

X = df[features]
y = df[target]