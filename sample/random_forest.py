from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import category_encoders as ce
import pandas as pd
import numpy as np
import joblib

# ======================================

print("Reading in labeled dataset sample...")
print()

df = pd.read_csv("C:\\Users\\ajaco\\Desktop\\repos\\noreallyimfine\\ebird-project\\data\\labelled_bird_sample.csv")
assert(df.shape == (103992, 16))

# ========================================

print("Select features and target to split dataframe into X and y...")
print()

features = ['name', 'season', 'region']
target = 'target'

X = df[features]
y = df[target]

assert(X.shape == (103992, 3))
assert(y.shape == (103992,))

# Saving list of birds, seasons, and regions
birds_list = X['name'].unique().tolist()
seasons_list = X['season'].unique().tolist()
regions_list = X['region'].unique().tolist()

joblib.dump(birds_list, 'sample/birds_list.joblib')
joblib.dump(seasons_list, 'sample/seasons_list.joblib')
joblib.dump(regions_list, 'sample/regions_list.joblib')
# =======================================

print("Encoding categorical features...")
print()

encoder = ce.CatBoostEncoder()

X = encoder.fit_transform(X, y)

# ======================================

print("Splitting X and y into train and test...")
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

assert(X_train.shape == (83193, 3))
assert(X_test.shape == (20799, 3))
assert(y_train.shape == (83193,))
assert(y_test.shape == (20799,))

# =====================================

print("Training Random Forest Classifier...")
print()

model = RandomForestClassifier(n_estimators=500, max_depth=None, random_state=42)
model.fit(X_train, y_train)

# =====================================

print("Making predictions and fetching score...")
print()

preds = model.predict(X_test)

print("\n\n")
print("ACCURACY SCORE: ")
print("================")
print(f"    {accuracy_score(y_test, preds)}    ")
print("================")
print("\n\n")
# =======================================

print("Saving encoder and model... ")
print()

joblib.dump(model, "rf.joblib")
joblib.dump(encoder, "cat_boost.joblib")
