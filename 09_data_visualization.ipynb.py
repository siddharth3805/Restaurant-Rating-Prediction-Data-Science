# ================================
# LEVEL 3 – TASK 3
# Data Visualization
# ================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# 1. Load Dataset
# ---------------------------

df = pd.read_csv("C:/Users\hp\Desktop\Dataset_Level2_Task3_FeatureEngineered.csv")

print("Dataset Loaded for LEVEL 3 TASK 3")
print(df.head())


# ---------------------------
# 2. Rating Distribution
# ---------------------------

plt.figure(figsize=(8,5))
plt.hist(df['Aggregate rating'], bins=20, edgecolor='black', color='skyblue')
plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()


# ---------------------------
# 3. Average Rating by City (Top 15)
# ---------------------------

top_cities = df['City'].value_counts().head(15).index
city_avg = df[df['City'].isin(top_cities)].groupby('City')['Aggregate rating'].mean().sort_values()

plt.figure(figsize=(12,6))
city_avg.plot(kind='barh', color='green')
plt.title("Average Rating of Top 15 Cities")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.tight_layout()
plt.show()


# ---------------------------
# 4. Average Rating by Cuisine (Top 15)
# ---------------------------

cuisine_exp = df['Cuisines'].dropna().str.split(',').explode().str.strip()
cuisine_avg = pd.DataFrame({
    "Cuisine": cuisine_exp,
    "Rating": df.loc[cuisine_exp.index, "Aggregate rating"]
})

top_cuisines = cuisine_avg['Cuisine'].value_counts().head(15).index
cuisine_rating_avg = cuisine_avg[cuisine_avg['Cuisine'].isin(top_cuisines)] \
                     .groupby('Cuisine')['Rating'].mean().sort_values()

plt.figure(figsize=(12,6))
cuisine_rating_avg.plot(kind='bar', color='orange')
plt.title("Average Rating of Top 15 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 5. Relationship: Price Range vs Rating
# ---------------------------

plt.figure(figsize=(8,5))
sns.boxplot(x='Price range', y='Aggregate rating', data=df, palette='Set2')
plt.title("Rating vs Price Range")
plt.xlabel("Price Range")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 6. Votes vs Rating Scatter Plot
# ---------------------------

plt.figure(figsize=(8,5))
plt.scatter(df['Votes'], df['Aggregate rating'], alpha=0.5, color='purple')
plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 7. Correlation Heatmap of Numerical Features
# ---------------------------

plt.figure(figsize=(10,6))
numerical_df = df.select_dtypes(include=['int64', 'float64'])
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()


print("\n✅ LEVEL 3 – TASK 3 Completed Successfully!")
