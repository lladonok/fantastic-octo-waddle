import pandas as pd

customers = pd.read_csv('All_Files/customers.csv')
orders = pd.read_csv('All_Files/orders.csv')

customers['birth_date'] = customers['birth_date'].str.strip()
customers['birth_date'] = pd.to_datetime(customers['birth_date'])
customers = customers[customers['birth_date'].notna()]

merged = customers.merge(orders, on='customer_id')

filtered = merged[merged['birth_date'].dt.year == 1990]

print(filtered[['order_id', 'customer_id']])