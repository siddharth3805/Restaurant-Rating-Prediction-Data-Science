# ================================
# LEVEL 1 – TASK 1
# Data Exploration & Preprocessing
# ================================

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 2. Load the dataset
# ---------------------------
# If your file is in same folder as notebook/script:
# file_path = "Dataset .csv"
# Else give full path like: r"C:\Users\YourName\Downloads\Dataset .csv"

file_path = "C:/Users\hp\Desktop\Dataset .csv"
df = pd.read_csv(file_path, encoding="utf-8")

print("✅ Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

# ---------------------------
# 3. Basic info: shape & dtypes
# ---------------------------

print("\nShape of dataset (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types (before cleaning):")
print(df.dtypes)

# ---------------------------
# 4. Missing values (before cleaning)
# ---------------------------

print("\nMissing values per column (count):")
missing_count = df.isna().sum()
print(missing_count)

print("\nMissing values percentage per column:")
missing_percent = (missing_count / len(df)) * 100
print(missing_percent.round(2))

# Create a summary table (optional but good for report)
missing_summary = pd.DataFrame({
    "missing_count": missing_count,
    "missing_percent": missing_percent.round(2)
})
print("\nMissing values summary table:")
print(missing_summary)

# ---------------------------
# 5. Handle missing values
# ---------------------------
# We will:
# - Fill numeric NaNs with median
# - Fill categorical NaNs with mode

df_clean = df.copy()

# Identify numeric & categorical columns
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df_clean.select_dtypes(exclude=[np.number]).columns.tolist()

print("\nNumeric columns:", numeric_cols)
print("Categorical columns:", categorical_cols)

# Fill numeric NaNs with median
for col in numeric_cols:
    if df_clean[col].isna().any():
        median_val = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_val)
        print(f"Filled NaNs in numeric column '{col}' with median: {median_val}")

# Fill categorical NaNs with mode
for col in categorical_cols:
    if df_clean[col].isna().any():
        mode_val = df_clean[col].mode()
        if not mode_val.empty:
            mode_val = mode_val[0]
            df_clean[col] = df_clean[col].fillna(mode_val)
            print(f"Filled NaNs in categorical column '{col}' with mode: {mode_val}")

# ---------------------------
# 6. Convert data types if needed
# ---------------------------
# These columns should be numeric. If they are objects, convert them.

cols_to_convert = ["Aggregate rating", "Votes", "Average Cost for two", "Price range"]

for col in cols_to_convert:
    if col in df_clean.columns:
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")

print("\nData types AFTER conversion:")
print(df_clean.dtypes)

# Check missing again after conversion & filling
missing_count_after = df_clean.isna().sum()
missing_percent_after = (missing_count_after / len(df_clean)) * 100

missing_summary_after = pd.DataFrame({
    "missing_count_after": missing_count_after,
    "missing_percent_after": missing_percent_after.round(2)
})
print("\nMissing values summary AFTER cleaning:")
print(missing_summary_after)

# ---------------------------
# 7. Analyze target variable: 'Aggregate rating'
# ---------------------------

target_col = "Aggregate rating"

if target_col in df_clean.columns:
    target = df_clean[target_col].dropna()
    # target_log= np.log1p(target)


    print(f"\nDescriptive statistics of '{target_col}':")
    print(target.describe())

    print(f"\nValue counts of '{target_col}' (class distribution):")
    print(target.value_counts().sort_index())

    # Class imbalance comment (basic)
    print("\nYou can inspect the above value_counts to see")
    print("if some rating values have very few samples (class imbalance).")

    # ---------------------------
    # 8. Plot distribution of 'Aggregate rating'
    # ---------------------------

    plt.figure(figsize=(8, 5))
    plt.hist(target, bins=20, edgecolor="black")
    # plt.hist(target_log, bins=20, edgecolor="black")
    plt.xlabel("Aggregate rating")
    plt.ylabel("Number of restaurants")
    plt.title("Distribution of Aggregate Rating")
    plt.tight_layout()
    plt.show()
else:
    print(f"\nColumn '{target_col}' not found in dataset.")

# ---------------------------
# 9. Save cleaned dataset (optional but recommended)
# ---------------------------

output_path = "Dataset_clean_Level1_Task1.csv"
df_clean.to_csv(output_path, index=False)
print(f"\n💾 Cleaned dataset saved as: {output_path}")
