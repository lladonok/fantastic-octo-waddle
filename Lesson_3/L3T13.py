import pandas as pd

contacts = pd.read_csv('All_Files/contacts.csv')
customers = pd.read_csv('All_Files/customers.csv')
orders = pd.read_csv('All_Files/orders.csv')

orders['order_date'] = pd.to_datetime(orders['order_date'].str.strip())

merged = orders.merge(customers, on='customer_id', how='left')\
                 .merge(contacts, on='customer_id', how='left')

EC_and_R = ['Germany', 'France', 'Italy', 'Spain', 'Russia', 'UK']  

merged['order_quarter'] = merged['order_date'].dt.quarter
merged['order_year'] = merged['order_date'].dt.year

filtered = merged.query(
    "country in @EC_and_R and "
    "order_quarter in [1, 2] and "
    "order_year == 2023"
)[['order_id', 'total']]

total_sum = filtered['total'].sum()
print(total_sum)