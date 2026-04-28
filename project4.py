import pandas as pd

# =========================
# 1. Create products.csv
# =========================
data = [
    [1, "Electronics", 1000],
    [2, "Clothing", 500],
    [3, "Electronics", 2000],
    [4, "Furniture", 1500],
    [5, "Electronics", 750],
]

df = pd.DataFrame(data, columns=["Product_ID", "Category", "Price"])
df.to_csv("products.csv", index=False)

# =========================
# 2. Product Class
# =========================
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        self.price = self.price * (1 - percent_off / 100)
        return self.price

# =========================
# 3. Load CSV
# =========================
df = pd.read_csv("products.csv")

# =========================
# 4. Filter Electronics
# =========================
electronics_df = df[df["Category"] == "Electronics"].copy()

# =========================
# 5. Apply 20% Discount
# =========================
new_prices = []

for _, row in electronics_df.iterrows():
    product = Product(row["Product_ID"], row["Price"])
    new_price = product.apply_discount(20)
    new_prices.append(new_price)

electronics_df["Price"] = new_prices
electronics_df["Promo_Active"] = "Yes"

# =========================
# 6. Save Excel File
# =========================
electronics_df.to_excel("holiday_promos.xlsx", index=False)

print("✅ Done! File saved as holiday_promos.xlsx")

