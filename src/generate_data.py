import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# -----------------------------
# CONFIG
# -----------------------------
num_days = 180
start_date = datetime(2024, 1, 1)

categories = {
    "Food": (100, 500),
    "Transport": (50, 300),
    "Shopping": (500, 5000),
    "Bills": (1000, 3000),
    "Entertainment": (200, 1500),
    "Healthcare": (300, 2000),
    "Travel": (1000, 8000),
    "Rent": (8000, 15000)
}

payment_methods = ["Cash", "UPI", "Card"]

data = []

# -----------------------------
# GENERATE DATA
# -----------------------------
for i in range(num_days):
    current_date = start_date + timedelta(days=i)

    # Daily expenses count
    num_transactions = random.randint(1, 5)

    for _ in range(num_transactions):
        category = random.choice(list(categories.keys()))
        min_amt, max_amt = categories[category]

        # Rent only once a month
        if category == "Rent" and current_date.day != 1:
            continue

        # Travel less frequent
        if category == "Travel" and random.random() > 0.2:
            continue

        amount = round(random.uniform(min_amt, max_amt), 2)

        data.append({
            "Date": current_date,
            "Category": category,
            "Amount": amount,
            "Payment_Method": random.choice(payment_methods)
        })

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data)

# Shuffle data
df = df.sample(frac=1).reset_index(drop=True)

# -----------------------------
# SAVE DATA
# -----------------------------
df.to_csv("data/expenses.csv", index=False)

print("Dataset generated successfully!")
print(df.head())