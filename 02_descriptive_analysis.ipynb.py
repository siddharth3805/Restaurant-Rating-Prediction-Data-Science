# ================================
# LEVEL 1 – TASK 2
# Descriptive Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load CLEANED dataset
# ---------------------------

df = pd.read_csv("C:/Users\hp\Desktop\Dataset .csv")

print("Dataset Loaded Successfully for Task 2!")
print(df.head())

# ---------------------------
# 2. Summary Statistics
# ---------------------------

print("\n📌 Numerical Column Summary:")
print(df.describe())

print("\n📌 Categorical Column Summary:")
print(df.describe(include='object'))

# ---------------------------
# 3. Distribution of Categorical Columns
# ---------------------------

# Country Distribution
plt.figure(figsize=(10,5))
df['Country Code'].value_counts().plot(kind='bar')
plt.title("Restaurant Distribution by Country Code")
plt.xlabel("Country Code")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# City Distribution (Top 20)
plt.figure(figsize=(12,6))
df['City'].value_counts().head(20).plot(kind='bar')
plt.title("Top 20 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# ---------------------------
# 4. Top Cuisines
# ---------------------------

# Split cuisines (many restaurants have multiple cuisines like 'North Indian, Chinese')
cuisine_series = df['Cuisines'].dropna().str.split(',').explode().str.strip()

top_cuisines = cuisine_series.value_counts().head(20)

print("\n📌 Top 20 Cuisines:")
print(top_cuisines)

plt.figure(figsize=(12,6))
top_cuisines.plot(kind='bar')
plt.title("Top 20 Most Popular Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ---------------------------
# 5. Top Cities with Most Restaurants
# ---------------------------

top_cities = df['City'].value_counts().head(10)

print("\n📌 Top 10 Cities with Most Restaurants:")
print(top_cities)

plt.figure(figsize=(10,5))
top_cities.plot(kind='bar')
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ---------------------------
# 6. Average Rating by City (Top 10 Cities)
# ---------------------------

avg_rating_city = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False).head(10)

print("\n📌 Top 10 Cities by Average Rating:")
print(avg_rating_city)

plt.figure(figsize=(10,5))
avg_rating_city.plot(kind='bar', color='green')
plt.title("Top 10 Cities by Average Aggregate Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

print("\n✅ LEVEL 1 – TASK 2 Completed Successfully!")
