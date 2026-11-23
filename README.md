# Retail Sales Data Engineering Project

## Project Overview
Developed an end-to-end Retail Sales Data Pipeline to extract, clean, transform, validate, and load retail sales data for analytical reporting.

## Technologies Used
- **Python:** ETL pipeline development
- **Pandas:** Data cleaning and transformation
- **MySQL:** Relational database storage
- **Google BigQuery:** Cloud data warehouse and analytics
- **SQL:** Joins, aggregations, and analytical queries
- **Git & GitHub:** Version control and project management

## Project Architecture

CSV Files → Python ETL Pipeline → Data Validation → MySQL → BigQuery → SQL Analytics

## Project Structure

```text
Retail_Sales_Data_Engineering/
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── export_bigquerry.py
├── output/
├── run_pipeline.py
└── README.md
```

## ETL Process

1. **Extract:** Read customer, product, and order CSV files using Python and Pandas.
2. **Transform:** Remove duplicates, join datasets, and calculate total sales.
3. **Validate:** Check missing values, duplicate records, invalid quantities, and sales calculations.
4. **Load:** Load transformed sales data into MySQL using SQLAlchemy.
5. **Automate:** Execute the ETL scripts using a single Python command.
6. **Analyze:** Upload processed data to BigQuery and perform analytical SQL queries.

## Data Warehouse Design

Implemented a Star Schema consisting of:

- `fact_sales`
- `dim_customer`
- `dim_product`
- `dim_date`

Used SQL joins to combine fact and dimension tables for analytical reporting.

## Project Results

- Total Orders: 5
- Total Items Sold: 15
- Total Revenue: ₹169,000
- Data validation: Successful
- MySQL and BigQuery revenue verification: Successful

## How to Run

Install required Python packages:

```bash
python -m pip install pandas numpy sqlalchemy pymysql google-cloud-bigquery google-cloud-storage
```

Execute the complete ETL pipeline:

```bash
python run_pipeline.py
```

## Author
Gajanan Shinde