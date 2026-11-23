import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

#Define project folders
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

#Read transformed CSV
sales = pd.read_csv(OUTPUT_DIR / "transformed_sales.csv ")

# MySQL connection details
username ="root"
password = "root"
host = "localhost"
database = "retail_sales_db"

#Create databse connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Load data into MySQL
sales.to_sql(
    name="sales",
    con = engine,
    if_exists="replace",
    index = False
)

print("Data loaded into MySQL successfully!")