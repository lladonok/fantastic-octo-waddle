import pandas as pd

products = pd.read_csv('All_Files/products.csv')

filtered = products[
    (products['price'] < 500) & 
    (products['volume_ml'] == 5.0)
]

print(filtered[['product_name', 'price']])