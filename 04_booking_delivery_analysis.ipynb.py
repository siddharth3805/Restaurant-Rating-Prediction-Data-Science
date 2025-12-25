# ================================
# LEVEL 2 – TASK 1
# Table Booking & Online Delivery Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load CLEANED dataset
# ---------------------------
df = pd.read_csv("C:/Users\hp\Desktop\Dataset .csv")

print("Dataset Loaded for LEVEL 2 TASK 1")
print(df[['Has Table booking', 'Has Online delivery', 'Aggregate rating', 'Price range']].head())


# ---------------------------
# 2. Percentage of Restaurants with Table Booking
# ---------------------------
table_booking_counts = df['Has Table booking'].value_counts()

print("\n📌 Table Booking Availability:")
print(table_booking_counts)

percentage_with_table_booking = (table_booking_counts.get('Yes', 0) / len(df)) * 100
percentage_without_table_booking = (table_booking_counts.get('No', 0) / len(df)) * 100

print(f"\nPercentage WITH Table Booking: {percentage_with_table_booking:.2f}%")
print(f"Percentage WITHOUT Table Booking: {percentage_without_table_booking:.2f}%")

# Bar chart
plt.figure(figsize=(6,4))
table_booking_counts.plot(kind='bar', color=['green', 'red'])
plt.title("Table Booking Availability")
plt.xlabel("Has Table Booking")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()


# ---------------------------
# 3. Compare Average Ratings (With vs Without Table Booking)
# ---------------------------
avg_rating_with = df[df['Has Table booking'] == 'Yes']['Aggregate rating'].mean()
avg_rating_without = df[df['Has Table booking'] == 'No']['Aggregate rating'].mean()

print("\n📌 Average Rating Comparison:")
print(f"Average Rating WITH Table Booking: {avg_rating_with:.2f}")
print(f"Average Rating WITHOUT Table Booking: {avg_rating_without:.2f}")

# Bar plot
plt.figure(figsize=(6,4))
plt.bar(['With Booking', 'Without Booking'],
        [avg_rating_with, avg_rating_without],
        color=['blue', 'orange'])
plt.title("Average Rating: Table Booking Comparison")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()


# ---------------------------
# 4. Online Delivery Availability Across Price Ranges
# ---------------------------
delivery_by_price = df.groupby('Price range')['Has Online delivery'].value_counts().unstack().fillna(0)

print("\n📌 Online Delivery Availability by Price Range:")
print(delivery_by_price)

# Stacked Bar Chart
delivery_by_price.plot(kind='bar', figsize=(8,5), stacked=True)
plt.title("Online Delivery Availability Across Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.legend(title="Has Online Delivery")
plt.tight_layout()
plt.show()


print("\n✅ LEVEL 2 – TASK 1 Completed Successfully!")
