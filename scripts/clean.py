import pandas as pd

df = pd.read_csv('/opt/airflow/data/raw_sales.csv')

# Remove null customer IDs
df = df.dropna(subset=['CustomerID'])

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid quantity
df = df[df['Quantity'] > 0]

# Convert datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Save clean data
df.to_csv('/opt/airflow/data/clean_sales.csv', index=False)

print("Cleaning Complete")