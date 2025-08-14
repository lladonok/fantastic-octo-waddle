import pandas as pd

customers = pd.read_csv('All_Files/customers.csv')

customers['birth_date'] = customers['birth_date'].str.strip()
customers['birth_date'] = pd.to_datetime(customers['birth_date'])
customers = customers[customers['birth_date'].notna()]

filtered = customers[
    (customers['gender'] == 'F') & 
    (customers['birth_date'].dt.year < 1995)
]

print(filtered[['customer_id', 'first_name', 'last_name', 'birth_date']])