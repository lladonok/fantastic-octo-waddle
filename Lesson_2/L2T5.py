import pandas as pd

orders = pd.read_csv('All_Files/orders.csv')

filtered = orders[
    (orders['customer_id'] >= 10) & 
    (orders['customer_id'] <= 20) &
    (orders['total'] > 8000)
]

print(filtered[['order_id', 'customer_id', 'total']])