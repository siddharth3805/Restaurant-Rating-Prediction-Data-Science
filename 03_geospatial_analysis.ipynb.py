# ================================
# LEVEL 1 – TASK 3
# Geospatial Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load Cleaned Dataset
# ---------------------------

df = pd.read_csv("C:/Users\hp\Desktop\Dataset .csv")

print("Dataset Loaded for Task 3!")
print(df[['Longitude', 'Latitude', 'City', 'Country Code', 'Aggregate rating']].head())

# ---------------------------
# 2. Basic Check for Coordinates
# ---------------------------

print("\nMissing values in Latitude and Longitude:")
print(df[['Latitude', 'Longitude']].isna().sum())

# Drop rows where coordinates are missing (if any)
df_geo = df.dropna(subset=['Latitude', 'Longitude'])

# ---------------------------
# 3. Plot Restaurants on Map (Scatter Plot)
# ---------------------------

plt.figure(figsize=(8,6))
plt.scatter(df_geo['Longitude'], df_geo['Latitude'],
            s=10, alpha=0.5, c='red')

plt.title("Restaurant Locations (Longitude vs Latitude)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

# ---------------------------
# 4. Distribution of Restaurants by Country
# ---------------------------

country_counts = df['Country Code'].value_counts()

print("\n📌 Restaurant Count by Country Code:")
print(country_counts)

plt.figure(figsize=(10,5))
country_counts.plot(kind='bar')
plt.title("Restaurant Count by Country Code")
plt.xlabel("Country Code")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# ---------------------------
# 5. Distribution of Restaurants by City (Top 20)
# ---------------------------

city_counts = df['City'].value_counts().head(20)

print("\n📌 Top 20 Cities with Most Restaurants:")
print(city_counts)

plt.figure(figsize=(12,6))
city_counts.plot(kind='bar')
plt.title("Top 20 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Restaurant Count")
plt.tight_layout()
plt.show()

# ---------------------------
# 6. Location vs Rating Analysis
# ---------------------------

plt.figure(figsize=(8,6))
plt.scatter(df_geo['Longitude'], df_geo['Latitude'],
            c=df_geo['Aggregate rating'], cmap='viridis', s=20)

plt.colorbar(label="Rating")
plt.title("Restaurant Ratings Across Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()

print("\n📌 Insight:")
print("Higher rated restaurants may show clustering patterns when viewed geographically.")

print("\n✅ LEVEL 1 – TASK 3 Completed Successfully!")
