# ================================
# LEVEL 2 – TASK 2
# Price Range Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load Cleaned Dataset
# ---------------------------
df = pd.read_csv("C:/Users\hp\Desktop\Dataset .csv")

print("Dataset Loaded for LEVEL 2 TASK 2")
print(df[['Price range', 'Aggregate rating', 'Rating color']].head())


# ---------------------------
# 2. Most Common Price Range
# ---------------------------
price_counts = df['Price range'].value_counts()

most_common_price = price_counts.idxmax()

print("\n📌 Price Range Frequency:")
print(price_counts)

print(f"\n👉 The MOST COMMON price range is: {most_common_price}")


# Bar chart for price ranges
plt.figure(figsize=(6,4))
price_counts.plot(kind='bar', color='skyblue')
plt.title("Most Common Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()


# ---------------------------
# 3. Average Rating for Each Price Range
# ---------------------------
avg_rating_per_price = df.groupby('Price range')['Aggregate rating'].mean().round(2)

print("\n📌 Average Rating per Price Range:")
print(avg_rating_per_price)

# Bar chart for avg ratings
plt.figure(figsize=(6,4))
avg_rating_per_price.plot(kind='bar', color='green')
plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 4. Rating Color with Highest Average Rating
# ---------------------------
avg_rating_by_color = df.groupby('Rating color')['Aggregate rating'].mean().round(2)

best_color = avg_rating_by_color.idxmax()
best_color_rating = avg_rating_by_color.max()

print("\n📌 Average Rating by Rating Color:")
print(avg_rating_by_color)

print(f"\n👉 Rating color with the HIGHEST average rating: {best_color} ({best_color_rating})")

# Bar plot for rating colors
plt.figure(figsize=(7,4))
avg_rating_by_color.plot(kind='bar', color='purple')
plt.title("Average Rating by Rating Color")
plt.xlabel("Rating Color")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


print("\n✅ LEVEL 2 – TASK 2 Completed Successfully!")
