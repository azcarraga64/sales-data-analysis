import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv")

print(df.head())

# Sales by category
category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)

category_sales.plot(kind="bar", title="Sales by Category")

plt.show()

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()

region_sales.plot(kind="bar", title="Sales by Region")

plt.show()

# Top products
top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)

print(top_products)

top_products.plot(kind="bar", title="Top Products")

plt.show()
