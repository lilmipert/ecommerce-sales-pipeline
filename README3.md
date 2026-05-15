🛒 E-Commerce Sales Analytics Pipeline

---

 📌 Project Overview

This project is an **end-to-end Data Engineering pipeline** designed to process and analyze e-commerce transaction data using **Apache Airflow, PostgreSQL, Docker, and Metabase**.

The main objective is to automate the full ETL workflow—from raw data ingestion to business intelligence visualization—while demonstrating modern Data Engineering concepts such as:

- Workflow orchestration
- ETL pipeline design
- Data warehousing
- Containerization
- Analytical dashboarding

The system processes the **Online Retail dataset**, performs data cleaning and transformation, generates business KPIs, stores data in PostgreSQL, and visualizes insights using Metabase.

---

✨ Key Features

- Automated ETL pipeline using Apache Airflow
- Containerized infrastructure with Docker & Docker Compose
- Multi-layer architecture (Bronze / Silver / Gold)
- Data cleaning and validation using Pandas
- PostgreSQL Data Warehouse integration
- SQL-based analytics layer
- Interactive dashboards using Metabase
- Modular and scalable ETL design

---

 🏗️ Architecture Diagram (End-to-End Pipeline)

```mermaid
graph TD

A[Online Retail CSV Dataset] --> B[Apache Airflow]

subgraph Bronze Layer
B1[Ingest Raw Data]
B2[Raw Sales Dataset]
B1 --> B2
end

subgraph Silver Layer
C1[Clean & Validate Data]
C2[clean_sales Table]
C1 --> C2
end

subgraph Gold Layer
D1[Transform Analytics]
D2[sales_summary Table]
D1 --> D2
end

subgraph Serving Layer
E1[(PostgreSQL)]
F1[Metabase Dashboard]
E1 --> F1
end

B --> B1
B2 --> C1
C2 --> D1
D2 --> E1

F1 --> H1[Total Revenue]
F1 --> H2[Monthly Revenue Trend]
F1 --> H3[Top Products]
F1 --> H4[Top Customers]
F1 --> H5[Revenue by Country]
````

---

🔄 ETL Pipeline Workflow (Sequence Diagram)

```mermaid
sequenceDiagram
participant User
participant Airflow
participant Python
participant Postgres
participant Metabase

User->>Airflow: Trigger DAG execution
Airflow->>Python: Run ingestion task
Python->>Postgres: Load Bronze data

Airflow->>Python: Run cleaning task
Python->>Postgres: Load Silver data

Airflow->>Python: Run transformation task
Python->>Postgres: Load Gold tables

Metabase->>Postgres: Query analytics tables
Postgres-->>Metabase: Return KPIs & insights
```

---

 🛠️ Dataset & Tech Stack

📊 Dataset

**Online Retail Dataset (Kaggle)**

Includes:

* Invoice transactions
* Product descriptions
* Quantity sold
* Unit price
* Customer IDs
* Timestamp data
* Country information

---

💻 Tech Stack

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Apache Airflow | Workflow orchestration |
| Docker         | Containerization       |
| Python         | ETL scripting          |
| Pandas         | Data processing        |
| PostgreSQL     | Data warehouse         |
| SQLAlchemy     | DB connection          |
| Metabase       | Data visualization     |

---

#📂 Project Structure

```bash
ecommerce-pipeline/
│
├── dags/
│   └── ecommerce_pipeline.py
│
├── scripts/
│   ├── ingest.py
│   ├── clean.py
│   ├── transform.py
│   └── load.py
│
├── data/
│   └── Online Retail.csv
│
├── sql/
├── logs/
├── plugins/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── images/
    ├── airflow.png
    ├── dashboard.png
    └── architecture.png
```

---

⚙️ Data Pipeline Layers

---

 🥉 Bronze Layer (Raw Data Ingestion)

* Load raw CSV data
* Preserve original dataset
* Ensure reproducibility

```python
df = pd.read_csv('/opt/airflow/data/Online Retail.csv')
```

---

🥈 Silver Layer (Data Cleaning)

* Remove null CustomerID
* Remove duplicates
* Filter invalid values
* Standardize datetime

```python
df = df.dropna(subset=["CustomerID"])
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
```

---

 🥇 Gold Layer (Business Analytics)
* Revenue calculation
* KPI aggregation
* Reporting tables

```python
df["revenue"] = df["Quantity"] * df["UnitPrice"]

monthly_sales = df.groupby(
    df["InvoiceDate"].dt.to_period("M")
)["revenue"].sum()
```

---

 🌬️ Airflow DAG Workflow

```text
ingest_data
    ↓
clean_data
    ↓
transform_data
    ↓
load_to_postgres
```

---

🐳 Docker Setup

requirements.txt

```txt
pandas
sqlalchemy
psycopg2-binary
```

---

 Dockerfile

```dockerfile
FROM apache/airflow:2.9.1

USER airflow

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
```

---

docker-compose.yml (core services)

```yaml
services:
  airflow:
    image: apache/airflow:2.9.1
    container_name: airflow

  postgres:
    image: postgres:15
    container_name: postgres

  metabase:
    image: metabase/metabase:latest
    container_name: metabase
```

---

🚀 Setup Instructions

```bash
git clone https://github.com/lilmipert/ecommerce-sales-pipeline.git
cd ecommerce-sales-pipeline
docker compose up --build -d
```

---

🌐 Access Services

Airflow UI

```text
http://localhost:8080
```

 Metabase

```text
http://localhost:3000
```

---

🐘 PostgreSQL Config

| Key      | Value     |
| -------- | --------- |
| Host     | postgres  |
| Port     | 5432      |
| DB       | ecommerce |
| User     | admin     |
| Password | admin     |

---

 📊 SQL Analytics

💰 Total Revenue

```sql
SELECT SUM(revenue)
FROM clean_sales;
```

---

📈 Monthly Trend

```sql
SELECT month, revenue
FROM sales_summary
ORDER BY month;
```

---

🏆 Top Products

```sql
SELECT "Description",
SUM(revenue) AS total_revenue
FROM clean_sales
GROUP BY "Description"
ORDER BY total_revenue DESC
LIMIT 10;
```

---

👤 Top Customers

```sql
SELECT "CustomerID",
SUM(revenue) AS total_spending
FROM clean_sales
GROUP BY "CustomerID"
ORDER BY total_spending DESC
LIMIT 10;
```

---

🌍 Revenue by Country

```sql
SELECT "Country",
SUM(revenue) AS total_revenue
FROM clean_sales
GROUP BY "Country"
ORDER BY total_revenue DESC;
```

---

📊 Metabase Dashboard

* Total Revenue KPI
* Monthly Trend Chart
* Top Products Ranking
* Customer Segmentation
* Country Revenue Map

---

 🧠 Business Insights

* Revenue peaks during holiday seasons (Q4)
* Small percentage of customers generate majority revenue
* UK dominates total revenue
* Certain SKUs drive disproportionate sales

---

🛑 Stop System

```bash
docker compose down
```

---

 📌 Future Improvements

* Real-time streaming (Kafka)
* Spark distributed processing
* Incremental ETL (CDC)
* Cloud deployment (AWS/GCP)
* Monitoring & alerting system

---

 👤 Author

**Purita Liewtrakoon**
66102010183


```

---


