import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker 

#load the data from the cv file
df = pd.read_csv('retail_dashboards.csv', encoding= 'latin-1')

# Global style settings
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = '#f8f8f8'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['font.family'] = 'sans-serif'

#CHART 1: Profit by Region
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(region_profit.index, region_profit.values, color=['#2ecc71','#3498db','#e67e22','#e74c3c'], width=0.5)

# Add value labels on top of each bar
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 500,
            f'${bar.get_height():,.0f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('Total Profit by Region', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Total Profit ($)', fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('chart1_profit_by_region.png', dpi=150)
plt.show()
print("Chart 1 saved.")

#CHART 2: Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(category_sales.index, category_sales.values,
              color=['#3498db','#2ecc71','#e67e22'], width=0.5)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 5000,
            f'${bar.get_height():,.0f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('Total Sales by Category', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Total Sales ($)', fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))
plt.tight_layout()
plt.savefig('chart2_sales_by_category.png', dpi=150)
plt.show()
print("Chart 2 saved.")

#CHART 3: Average Discount by Region
region_discount = df.groupby('Region')['Discount'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(region_discount.index, region_discount.values,
              color=['#e74c3c','#e67e22','#3498db','#2ecc71'], width=0.5)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2,
            bar.get_height() + 0.003,
            f'{bar.get_height()*100:.1f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_title('Average Discount by Region', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Region', fontsize=12)
ax.set_ylabel('Average Discount (%)', fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
plt.tight_layout()
plt.savefig('chart3_discount_by_region.png', dpi=150)
plt.show()
print("Chart 3 saved.")