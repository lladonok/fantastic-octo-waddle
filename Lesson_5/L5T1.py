import pandas as pd

users = pd.read_csv('All_Files/users_new.csv')
orders = pd.read_csv('All_Files/orders_new.csv')

merged = orders.merge(users, on='user_id')

north_ppl = users.query("region == 'North' & age < 30")
north_orders = orders[orders['user_id'].isin(north_ppl['user_id'])]

print(north_ppl)
print(north_orders)
print("Общее количество заказов:", len(north_orders))