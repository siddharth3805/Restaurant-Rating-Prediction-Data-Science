# ================================
# LEVEL 3 – TASK 2
# Customer Preference Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load Feature Engineered Dataset
# ---------------------------

df = pd.read_csv("C:/Users\hp\Desktop\Dataset_Level2_Task3_FeatureEngineered.csv")

print("Dataset Loaded for LEVEL 3 TASK 2")
print(df[['Cuisines', 'Aggregate rating', 'Votes']].head())


# ---------------------------
# 2. Split Cuisines into individual entries
# ---------------------------

cuisine_exploded = df['Cuisines'].dropna().str.split(',').explode().str.strip()

# Add ratings & votes back to exploded dataframe
cuisine_df = pd.DataFrame({
    'Cuisine': cuisine_exploded,
    'Rating': df.loc[cuisine_exploded.index, 'Aggregate rating'],
    'Votes': df.loc[cuisine_exploded.index, 'Votes']
})

print("\nSample of processed cuisine dataset:")
print(cuisine_df.head())


# ---------------------------
# 3. Most Popular Cuisines (based on Votes)
# ---------------------------

popular_cuisines = cuisine_df.groupby('Cuisine')['Votes'].sum().sort_values(ascending=False).head(20)

print("\n📌 Top 20 Most Popular Cuisines (by votes):")
print(popular_cuisines)

plt.figure(figsize=(12,6))
popular_cuisines.plot(kind='bar', color='orange')
plt.title("Top 20 Most Popular Cuisines (Votes)")
plt.xlabel("Cuisine")
plt.ylabel("Total Votes")
plt.tight_layout()
plt.show()


# ---------------------------
# 4. Highest Rated Cuisines (Average Rating)
# ---------------------------

avg_rating_cuisine = cuisine_df.groupby('Cuisine')['Rating'].mean().sort_values(ascending=False).head(20)

print("\n📌 Top 20 Highest Rated Cuisines:")
print(avg_rating_cuisine)

plt.figure(figsize=(12,6))
avg_rating_cuisine.plot(kind='bar', color='green')
plt.title("Top 20 Highest Rated Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 5. Rating Distribution for Popular Cuisines (>1000 votes)
# ---------------------------

popular_threshold = cuisine_df.groupby("Cuisine")["Votes"].sum()
top_cuisine_list = popular_threshold[popular_threshold > 1000].index

filtered_df = cuisine_df[cuisine_df["Cuisine"].isin(top_cuisine_list)]

plt.figure(figsize=(10,5))
filtered_df.boxplot(column='Rating', by='Cuisine', rot=45)
plt.title("Rating Distribution for Popular Cuisines")
plt.suptitle("")  # removes extra title
plt.xlabel("Cuisine")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


print("\n✅ LEVEL 3 – TASK 2 Completed Successfully!")
