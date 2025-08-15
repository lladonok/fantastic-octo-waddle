import pandas as pd

df = pd.read_csv('All_Files/group_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

avg_order_per_city = df.groupby('city')['total'].mean().reset_index()
avg_order_per_city = avg_order_per_city.sort_values('total', ascending=False)
top_cities = avg_order_per_city.head(3)

print(top_cities)