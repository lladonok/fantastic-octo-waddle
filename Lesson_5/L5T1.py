import pandas as pd

users = pd.read_csv('All_Files/users_new.csv')
orders = pd.read_csv('All_Files/orders_new.csv')

north_ppl = users.query("region == 'North' & age < 30")

user_orders_count = orders.groupby('user_id')['order_id'].count().reset_index()
user_orders_count.columns = ['user_id', 'order_count']

result = north_ppl.merge(user_orders_count, on='user_id')[['name', 'order_count']]

print(result)