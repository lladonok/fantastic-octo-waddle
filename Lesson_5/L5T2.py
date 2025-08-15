import pandas as pd

orders = pd.read_csv('All_Files/orders_new.csv')

orders['total'] = orders['price'] * orders['quantity']

product_c = orders.query("product == 'C' & total > 250")

output_columns = ['order_id', 'user_id', 'product', 'price', 'quantity', 'total', 'order_date']

print(product_c[output_columns])