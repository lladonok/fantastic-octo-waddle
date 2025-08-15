import pandas as pd

users = pd.read_csv('All_Files/users_new.csv')
orders = pd.read_csv('All_Files/orders_new.csv')

merged = orders.merge(users, on='user_id')

user_orders = orders.groupby('user_id')['order_id'].count().reset_index()
active_users = user_orders[user_orders['order_id'] > 1]
result = active_users.merge(users, on='user_id')[['name', 'order_id']]

print(result.to_string(index=False))