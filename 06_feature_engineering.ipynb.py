# ================================
# LEVEL 2 – TASK 3
# Feature Engineering
# ================================

import pandas as pd

# ---------------------------
# 1. Load Cleaned Dataset
# ---------------------------
df = pd.read_csv("C:/Users\hp\Desktop\Dataset .csv")

print("Dataset Loaded for LEVEL 2 TASK 3")
print(df.head())


# ---------------------------
# 2. Create Text-Based Features
# ---------------------------

# Length of restaurant name
df['Name_length'] = df['Restaurant Name'].astype(str).str.len()

# Length of address
df['Address_length'] = df['Address'].astype(str).str.len()

# Number of cuisines per restaurant
df['Cuisine_count'] = df['Cuisines'].astype(str).str.split(',').apply(len)

print("\n📌 Sample of New Text Features:")
print(df[['Restaurant Name', 'Name_length', 'Address', 'Address_length', 'Cuisines', 'Cuisine_count']].head())


# ---------------------------
# 3. Encode Yes/No Categorical Features
# ---------------------------

mapping = {'Yes': 1, 'No': 0}

df['Table_booking_encoded'] = df['Has Table booking'].map(mapping)
df['Online_delivery_encoded'] = df['Has Online delivery'].map(mapping)

print("\n📌 Encoded Feature Samples:")
print(df[['Has Table booking', 'Table_booking_encoded',
         'Has Online delivery', 'Online_delivery_encoded']].head())


# ---------------------------
# 4. Additional Useful Features
# ---------------------------

# High Rating Feature (binary)
df['High_rating'] = df['Aggregate rating'].apply(lambda x: 1 if x >= 4.0 else 0)

# Popularity Score (Votes * Rating)
df['Popularity_score'] = df['Votes'] * df['Aggregate rating']

print("\n📌 Additional Feature Samples:")
print(df[['Aggregate rating', 'Votes', 'High_rating', 'Popularity_score']].head())


# ---------------------------
# 5. Save the Feature-Engineered Dataset
# ---------------------------

output_file = "C:/Users\hp\Desktop\Dataset_Level2_Task3_FeatureEngineered.csv"
df.to_csv(output_file, index=False)

print(f"\n💾 Feature-engineered dataset saved as: {output_file}")
print("\n✅ LEVEL 2 – TASK 3 Completed Successfully!")
