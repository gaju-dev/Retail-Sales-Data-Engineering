import pandas as pd
from pathlib import Path

#Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "OUTPUT"

# Read source files
customers  = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR/"products.csv")
orders = pd.read_csv(DATA_DIR/"orders.csv")

#Read transformed sales data
sales = pd.read_csv(OUTPUT_DIR / "transformed_sales.csv")

print("=========DATA QUALITY REPORT=============")

# 1. check missing values
print("\n1.Misiing Values:")
print("Customers:", customers.isnull().sum().sum())
print("Products:", products.isnull().sum().sum())
print("Orders:", orders.isnull().sum().sum())
print("Sales:", sales.isnull().sum().sum())

# 2. Check duplicate records
print("\n2. Duplicate Records:")
print("Duplicate Customers:", customers["customer_id"].duplicated().sum())
print("Duplicate Products:", products["product_id"].duplicated().sum())
print("Duplicate Orders:", orders["order_id"].duplicated().sum())

# 3. Check missing customer and product matches
print("\n3. Invalid Vustomer/Product References:")
print("Missing Customer Matches:", sales["customer_name"].isnull().sum())
print("Missing Product Matches:", sales["product_name"].isnull().sum())

# 4. Check invalid quantities
print("\n4. Invalid Quantities:")
print("Invalid Quantity Records:", (sales["quantity"] <= 0).sum())

# 5. Verify sales calculations
sales["quantity"] = pd.to_numeric(sales["quantity"])
sales["price"] = pd.to_numeric(sales["price"])
sales["total_sales"] = pd.to_numeric(sales["total_sales"])

expected_sales = sales["quantity"]* sales["price"]

incorrect_sales_count = (
    sales["total_sales"] != expected_sales
).sum()

print("\n5. Sales Clculation Check:")
print("Incorrect Sales Records:", incorrect_sales_count)

# 6. Final Summary
print("\n6. Final Summary:")
print("Total Orders:", len(sales))
print("Total Revenue:", sales["total_sales"].sum())

missing_values = sales.isnull().sum().sum()
missing_customers = sales["customer_name"].isnull().sum()
missing_products = sales["product_name"].isnull().sum()
invalid_quantities = (sales["quantity"] <= 0).sum()
if(
    missing_values == 0
    and missing_customers == 0
    and invalid_quantities == 0
    and incorrect_sales_count == 0
):
    print("\nData validation completed successfully!")
else:
    print("\nData validation found issues. Please investigate.")
    raise SystemExit(1)
