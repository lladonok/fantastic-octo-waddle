import pandas as pd

orders = pd.read_csv('All_Files/orders.csv')
orders['order_date'] = orders['order_date'].str.strip()
orders['order_date'] = pd.to_datetime(orders['order_date'])

filtered = orders[
    (orders['total'] >= 30000) & 
    (orders['total'] <= 40000) &
    (orders['order_date'] >= '2023-01-01')
]

print(filtered['order_id'])

# у меня возникли некоторые проблемы, в файле с заказами есть лишние пробелы в некоторых значениях столбца order_date (например, строка 61), 
# так что пришлось экспериментировать с бубном чтобы код заработал... ПРОСТИТЕ если это не так, как в лекции 2
# (orders = pd.read_csv('All_Files\orders.csv',sep=',',encoding='utf-8')), но по-другому он не работал!!! (╥﹏╥)
