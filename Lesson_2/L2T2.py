import pandas as pd

orders = pd.read_csv('All_Files/orders.csv')

orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])
filtered = orders[orders['order_date'].notna()]
russian_orders = orders[
    (orders['customer_id'] >= 68) & 
    (orders['customer_id'] <= 88) &
    (orders['order_date'].dt.year == 2022)  
]

result = russian_orders.iloc[4:10][['order_id', 'total']]
print(result)