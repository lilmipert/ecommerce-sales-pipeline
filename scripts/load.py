import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine(
    'postgresql://admin:admin@postgres:5432/ecommerce'
)

# Read transformed files
sales = pd.read_csv('/opt/airflow/data/final_sales.csv')

summary = pd.read_csv(
    '/opt/airflow/data/sales_summary.csv'
)

# Load tables
sales.to_sql(
    'clean_sales',
    engine,
    if_exists='replace',
    index=False
)

summary.to_sql(
    'sales_summary',
    engine,
    if_exists='replace',
    index=False
)

print("Loaded to PostgreSQL")