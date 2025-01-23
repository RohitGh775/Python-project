import numpy as np
sales_data = np.array([
    [120, 100, 90, 150, 130, 110],  # January
    [150, 130, 110, 160, 140, 120],  # February
    [170, 160, 140, 180, 150, 130],  # March
    [200, 190, 160, 200, 170, 140],  # April
    [210, 200, 180, 220, 190, 160],  # May
    [230, 220, 200, 240, 210, 180],  # June
    [250, 240, 220, 260, 230, 200],  # July
    [260, 250, 230, 270, 240, 210],  # August
    [280, 270, 250, 290, 260, 230],  # September
    [300, 290, 270, 310, 280, 250],  # October
    [320, 310, 290, 330, 300, 270],  # November
    [340, 330, 310, 350, 320, 290],  # December
])
#Total sales for each product over the year
Total_sales=np.sum(sales_data, axis=0)
print(f'the sale for each year is:{Total_sales}')

# Total sales for each month
Total_salesmonth=np.sum(sales_data, axis=1)
print(f'Monthly sales is:{Total_salesmonth}')

# Average monthly sales for each product
Averagemonthly=np.mean(sales_data, axis=1)
print(f'Monthly averag sales is:{Averagemonthly}')

# Month with the highest total sales
highest_salesmonth = np.argmax(Total_salesmonth)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
print("Month with the highest sales:", months[highest_salesmonth])


#Highest product
highest_sales_product_index = np.argmax(Total_sales)
products = ["Product A", "Product B", "Product C", "Product D", "Product E", "Product F"]
print("Best performing product:", products[highest_sales_product_index])

#Percentage contribution of per product
Total_salesperproduct=np.sum(Total_sales)
Percontribution=(Total_sales/Total_salesperproduct)*100
print(f'Per Contribute of each product is:{Percontribution}')


#Monthly trends
for i, product in enumerate(products):
    print(f"{product}: {sales_data[:, i]}")