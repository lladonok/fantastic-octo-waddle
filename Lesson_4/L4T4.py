import pandas as pd

df = pd.read_csv('All_Files/group_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

df['month'] = df['order_date'].dt.to_period('M')  # Метод из лекции
revenue_per_month = df.groupby('month')['total'].sum().reset_index()
revenue_per_month.columns = ['Месяц', 'Общая выручка']

print(revenue_per_month)