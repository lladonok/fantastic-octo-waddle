import pandas as pd

df = pd.read_csv('All_Files/group_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

product_quantity = df.groupby('product')['quantity'].sum().reset_index()
top_product = product_quantity.loc[product_quantity['quantity'].idxmax()]

print(top_product['product'])
print(top_product['quantity'])