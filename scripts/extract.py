import pandas as pd
import os

#Define project data folder
from pathlib import Path
data_folder = Path(__file__).resolve().parent.parent / "data"

#Read source CSV files
customers = pd.read_csv(os.path.join(data_folder, "customers.csv"))
products = pd.read_csv(os.path.join(data_folder, "products.csv"))
orders = pd.read_csv(os.path.join(data_folder, "orders.csv"))

#Display extracted data
print("CUSTOMERS DATA")
print(customers)

print("\nPRODUCTS DATA")
print(products)

print("\nORDERS DATA")
print(orders)

print("\nData extraction completed successfully!")