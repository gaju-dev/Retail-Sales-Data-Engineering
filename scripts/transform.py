import pandas as pd
from pathlib import Path

#Define project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

#Read CSV files
customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")

# Remove duplicate records
customers = customers.drop_duplicates(subset=["customer_id"])
products = products.drop_duplicates(subset=["product_id"])
orders = orders.drop_duplicates(subset=["order_id"])

# Joinorders with customer details
sales = orders.merge(customers, on="customer_id", how="left")

#Join sales with product details
sales = sales.merge(products, on = "product_id", how="left")

#Calculate total sales
sales["total_sales"] = sales["quantity"]* sales["price"]

#Save transformed data
OUTPUT_DIR.mkdir(exist_ok=True)
sales.to_csv(OUTPUT_DIR /"transformed_sales.csv", index = False)

print("Data tranformation completed successfully!")
print(sales)