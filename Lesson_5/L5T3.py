import pandas as pd

users = pd.read_csv('All_Files/users_new.csv')
orders = pd.read_csv('All_Files/orders_new.csv')

product_counts = orders['product'].value_counts()

print(product_counts)
