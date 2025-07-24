import pandas as pd

# Sample Data
data = {
    "Date": pd.date_range(start="2023-01-01", periods=40).tolist(),
    "Region": (["North"] * 10 + ["South"] * 10 + ["East"] * 10 + ["West"] * 10),
    "Product": (["Laptop"] * 10 + ["Desk"] * 10 + ["Phone"] * 10 + ["Chair"] * 10),
    "Category": (["Electronics"] * 20 + ["Furniture"] * 20),
    "Sales": [1200] * 10 + [800] * 10 + [900] * 10 + [400] * 10,
    "Profit": [300] * 10 + [160] * 10 + [225] * 10 + [80] * 10,
    "Quantity": [5] * 10 + [2] * 10 + [3] * 10 + [4] * 10
}
df = pd.DataFrame(data)
