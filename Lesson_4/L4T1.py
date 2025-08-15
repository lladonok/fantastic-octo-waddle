import pandas as pd

df = pd.read_csv('All_Files/group_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

orders_per_city = df.groupby('city')['order_id'].nunique().reset_index()

print(orders_per_city)


