import pandas as pd

df = pd.read_csv('/opt/airflow/data/clean_sales.csv')

# Revenue calculation
df['revenue'] = df['Quantity'] * df['UnitPrice']

# Extract month
df['month'] = pd.to_datetime(df['InvoiceDate']).dt.month

# Monthly sales summary
sales_summary = (
    df.groupby('month')['revenue']
    .sum()
    .reset_index()
)

# Save outputs
df.to_csv('/opt/airflow/data/final_sales.csv', index=False)

sales_summary.to_csv(
    '/opt/airflow/data/sales_summary.csv',
    index=False
)

print("Transformation Complete")