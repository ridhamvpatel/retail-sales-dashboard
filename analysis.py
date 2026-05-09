import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('retail_dashboards.csv', encoding='latin-1')

#QUESTION 1: Which region is most profitable?
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("Profit by Region:")
print(region_profit)

# Plot it
region_profit.plot(kind='bar', color='steelblue', figsize=(8,5))
plt.title('Total Profit by Region')
plt.xlabel('Region')
plt.ylabel('Total Profit ($)')
plt.tight_layout()
plt.savefig('profit_by_region.png')
plt.show()
print("Chart saved!")

#Question 2: Which category drives the most revenue?
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

#Plot category sales
category_sales.plot(kind='bar', color = 'seagreen', figsize=(8,5))
plt.title("Total Sales by Category:")
plt.xlabel("Category")
plt.ylabel('Total Sales ($)')
plt.tight_layout()
plt.savefig("sales_by_category")
plt.show()
print("Chart saved")

#Question 3: Which regions give the most discounts?
region_discount = df.groupby("Region")["Discount"].mean().sort_values(ascending=False)
print('\nAverage Discounts by Region:')
print(region_discount)

#plot 
region_discount.plot(kind='bar', color = 'salmon', figsize=(8,5))
plt.title("Average Discounts by Region")
plt.xlabel("Region")
plt.ylabel("Average Discount")
plt.tight_layout()
plt.savefig('discount_by_region.png')
plt.show()
print("Chart saved.")
