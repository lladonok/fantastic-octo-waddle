import pandas as pd

orders = pd.read_csv('All_Files/orders.csv')

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders = orders[orders['order_date'].notna()]

filtered = orders[
    (orders['total'] >= 10000) & 
    (orders['total'] <= 15000) &
    (orders['order_date'].dt.year == 2023)
]

print(filtered[['order_id', 'total', 'order_date']])