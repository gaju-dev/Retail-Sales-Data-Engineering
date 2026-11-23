import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

sales = pd.read_csv(OUTPUT_DIR / "transformed_sales.csv")

# Create date_id in YYYMMDD format

sales["date_id"] = pd.to_datetime(
 sales["order_date"]
).dt.strftime("%Y%m%d").astype(int)

# Calculate total sales
sales["total_sales" ] = sales["quantity"]*sales["price"]

# Create the fact table
fact_sales = sales[
    [
        "order_id",
        "customer_id",
        "product_id",
        "date_id",
        "quantity",
        "total_sales"
    ]
]
fact_sales.to_csv(
    OUTPUT_DIR / "fact_sales.csv",
    index = False
)

print("Fact sales CSV created successfully!")
print(fact_sales)
