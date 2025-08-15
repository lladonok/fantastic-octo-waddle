import pandas as pd

df = pd.read_csv('All_Files/group_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

avg_order_per_city = df.groupby('city')['total'].mean().reset_index()

print(avg_order_per_city)