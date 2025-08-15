import pandas as pd

users = pd.read_csv('All_Files/users_new.csv')
orders = pd.read_csv('All_Files/orders_new.csv')

merged = orders.merge(users, on='user_id')
merged['total_sum'] = merged['price'] * merged['quantity']
table = merged.pivot_table(
    index='region',
    columns='product',
    values='total_sum',
    aggfunc='sum',
    fill_value=0
)

print(table)