import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/expenses.csv")

print("🔹 Raw Data Preview:")
print(df.head())

# -----------------------------
# BASIC INFO
# -----------------------------
print("\n🔹 Data Info:")
print(df.info())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# -----------------------------
# CLEANING STEPS
# -----------------------------

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=["Date"])

# Remove negative or zero expenses (if any)
df = df[df["Amount"] > 0]

# Standardize category names
df["Category"] = df["Category"].str.strip().str.title()

# Standardize payment methods
df["Payment_Method"] = df["Payment_Method"].str.strip().str.upper()

# Remove duplicates
df = df.drop_duplicates()

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
df["Day_Name"] = df["Date"].dt.day_name()

# -----------------------------
# SAVE CLEAN DATA
# -----------------------------
df.to_csv("data/cleaned_expenses.csv", index=False)

print("\nData cleaned successfully!")
print("\n🔹 Clean Data Preview:")
print(df.head())