# Commerce Quick-Start Demo (AgentDS-Bench)
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load sales history
sales = pd.read_csv("tabular/sales_history.csv")
sales['date'] = pd.to_datetime(sales['date'])  # Convert to datetime
print("✅ Loaded sales_history.csv")
print(sales.head())

# Load inventory log
inventory = pd.read_csv("tabular/inventory_log.csv")
inventory['date'] = pd.to_datetime(inventory['date'])  # Convert to datetime
print("✅ Loaded inventory_log.csv")
print(inventory.head())

# Load product catalog
products = pd.read_csv("tabular/products.csv")
print("✅ Loaded products.csv")
print(products[['product_id', 'name', 'category', 'price']].head())

# Load customer profiles
customers = pd.read_csv("tabular/customers.csv")
print("✅ Loaded customers.csv")
print(customers.head())

# Load a few user interactions from JSONL
print("✅ Loading interactions.jsonl")
with open("tabular/interactions.jsonl", "r") as f:
    interactions = [json.loads(next(f)) for _ in range(5)]
for i, event in enumerate(interactions, 1):
    print(f"Event {i}: {event}")

# Basic visualization: daily sales distribution
daily_sales = sales.groupby('date')['units_sold'].sum()
daily_sales.plot(title="Daily Units Sold (All Products)", figsize=(10, 4))
plt.xlabel("Date")
plt.ylabel("Units Sold")
plt.grid(True)
plt.tight_layout()
plt.show()

# Join sales and inventory to view stockouts
merged = pd.merge(sales, inventory, on=['date', 'store_id', 'product_id'], how='inner')
stockouts = merged[merged['closing_stock'] == 0]
print(f"⚠️ Found {len(stockouts)} stockout events")