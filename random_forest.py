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

assert(X.shape == (103992, 5))
assert(y.shape == (103992,))

# =======================================

print("Encoding categorical features...")
print()

encoder = ce.CatBoostEncoder()

X = encoder.fit_transform(X, y)

# ======================================

print("Splitting X and y into train and test...")
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

assert(X_train.shape == (83193, 5))
assert(X_test.shape == (20799, 5))
assert(y_train.shape == (83193,))
assert(y_test.shape == (20799,))

# =====================================

print("Training model...")
print()

model = RandomForestClassifier(n_estimators=1000, max_depth=None, random_state=42)
model.fit(X_train, y_train)

# =====================================