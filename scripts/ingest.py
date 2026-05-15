import pandas as pd

# Read original dataset
df = pd.read_csv('/opt/airflow/data/online_retail.csv')

print(df.head())

# Save raw data
df.to_csv('/opt/airflow/data/raw_sales.csv', index=False)

print("Ingestion Complete")