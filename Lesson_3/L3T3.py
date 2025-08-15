import pandas as pd

customers = pd.read_csv('All_Files/customers.csv')
orders = pd.read_csv('All_Files/orders.csv')

orders['order_date'] = pd.to_datetime(orders['order_date'].str.strip())

merged = orders.merge(customers, on='customer_id', how='left')

filtered = merged[
    merged['order_date'].dt.year.isin([2022, 2023])
]

gender_counts = filtered['gender'].value_counts()
print(gender_counts.to_string())