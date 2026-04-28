import pandas as pd

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def use_item(self, amount):
        self.quantity -= amount
        if self.quantity < 0:
            self.quantity = 0


# Load CSV
df = pd.read_csv("morning_stock.csv")

df.rename(columns={"Qty_kg": "Current_Quantity"}, inplace=True)

# Clean data (VERY IMPORTANT)
df["Ingredient_clean"] = df["Ingredient"].str.strip().str.lower()

# Find coffee beans safely
coffee_row = df[df["Ingredient_clean"] == "coffee beans"]

if coffee_row.empty:
    print("⚠ Coffee Beans not found — using default row for safety")

    # fallback: create default row update (so file still generates)
    df.to_csv("evening_stock.csv", index=False)
    print("✅ File still created without update")
    exit()

# Get values
name = coffee_row["Ingredient"].values[0]
qty = coffee_row["Current_Quantity"].values[0]

coffee = Ingredient(name, qty)
coffee.use_item(2.5)

# Update
df.loc[df["Ingredient_clean"] == "coffee beans", "Current_Quantity"] = coffee.quantity

# Save file
df.drop(columns=["Ingredient_clean"], inplace=True)
df.to_csv("evening_stock.csv", index=False)

print("✅ Evening stock created successfully!")
print(df)