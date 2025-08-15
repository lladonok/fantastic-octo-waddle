import pandas as pd

contacts = pd.read_csv('All_Files/contacts.csv')
customers = pd.read_csv('All_Files/customers.csv')
orders = pd.read_csv('All_Files/orders.csv')

customers['registration_date'] = pd.to_datetime(customers['registration_date'].str.strip())
orders['order_date'] = pd.to_datetime(orders['order_date'].str.strip())

merged = orders.merge(customers, on='customer_id', how='left')\
              .merge(contacts, on='customer_id', how='left')

filtered = merged.query(
    "registration_date >= '2022-01-01' and "
    "order_date.dt.year == 2023 and "
    "total > 30000"
)[['first_name', 'last_name', 'total']]

print(filtered.to_string(index=False))
print(f"\nКоличество продаж: {len(filtered)}")