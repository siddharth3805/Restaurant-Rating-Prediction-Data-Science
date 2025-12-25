# ================================
# LEVEL 3 – TASK 1
# Predictive Modeling: Predict Aggregate Rating
# ================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------
# 1. Load Feature Engineered Dataset
# ---------------------------
df = pd.read_csv("C:/Users\hp\Desktop\Dataset_Level2_Task3_FeatureEngineered.csv")

print("Dataset Loaded for LEVEL 3 TASK 1")
print(df.head())


# ---------------------------
# 2. Select Features & Target
# ---------------------------
# We drop non-numeric and irrelevant columns
features = df[[
    'Average Cost for two', 'Price range', 'Votes',
    'Name_length', 'Address_length', 'Cuisine_count',
    'Table_booking_encoded', 'Online_delivery_encoded',
    'High_rating', 'Popularity_score'
]]

target = df['Aggregate rating']


# ---------------------------
# 3. Split into Train/Test Sets
# ---------------------------

X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

print(f"\nTraining Samples: {len(X_train)}")
print(f"Testing Samples: {len(X_test)}")


# ---------------------------
# 4. Train Models
# ---------------------------

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Decision Tree
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

# Random Forest
rf_model = RandomForestRegressor(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)


# ---------------------------
# 5. Predictions
# ---------------------------

lr_pred = lr_model.predict(X_test)
dt_pred = dt_model.predict(X_test)
rf_pred = rf_model.predict(X_test)


# ---------------------------
# 6. Evaluation Function
# ---------------------------

def evaluate_model(name, y_test, y_pred):
    print(f"\n📌 MODEL: {name}")
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
    print("R² Score:", r2_score(y_test, y_pred))


# ---------------------------
# 7. Evaluate All Models
# ---------------------------

evaluate_model("Linear Regression", y_test, lr_pred)
evaluate_model("Decision Tree", y_test, dt_pred)
evaluate_model("Random Forest", y_test, rf_pred)

# ================================
# Random Forest Hyperparameter Tuning
# ================================

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Base model
rf = RandomForestRegressor(random_state=42)

# Parameter grid
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2']
}

# GridSearch
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    cv=5,
    scoring='r2',
    n_jobs=1,
    verbose=2
)

# Fit
grid_search.fit(X_train, y_train)

# Best model
best_rf = grid_search.best_estimator_

print("\n✅ Best Parameters Found:")
print(grid_search.best_params_)

# Evaluate best model
best_pred = best_rf.predict(X_test)

print("\n📊 Tuned Random Forest Performance:")
print("MAE:", mean_absolute_error(y_test, best_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, best_pred)))
print("R² Score:", r2_score(y_test, best_pred))


print("\n✅ LEVEL 3 – TASK 1 Completed Successfully!")
