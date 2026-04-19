import pandas as pd

# -----------------------------
# LOAD CLEAN DATA
# -----------------------------
df = pd.read_csv("data/cleaned_expenses.csv")

# -----------------------------
# FEATURE 1: WEEKEND / WEEKDAY
# -----------------------------
df["Day_Name"] = pd.to_datetime(df["Date"]).dt.day_name()

df["Is_Weekend"] = df["Day_Name"].isin(["Saturday", "Sunday"])

# -----------------------------
# FEATURE 2: SPENDING LEVEL
# -----------------------------
def spending_level(amount):
    if amount < 500:
        return "Low"
    elif amount < 2000:
        return "Medium"
    else:
        return "High"

df["Spending_Level"] = df["Amount"].apply(spending_level)

# -----------------------------
# FEATURE 3: EXPENSE TYPE
# -----------------------------
essential = ["Rent", "Bills", "Food", "Healthcare"]

df["Expense_Type"] = df["Category"].apply(
    lambda x: "Essential" if x in essential else "Non-Essential"
)

# -----------------------------
# FEATURE 4: MONTH NAME
# -----------------------------
df["Month_Name"] = pd.to_datetime(df["Date"]).dt.month_name()

# -----------------------------
# FEATURE 5: DAILY TOTAL SPENDING
# -----------------------------
daily_total = df.groupby("Date")["Amount"].sum().reset_index()
daily_total.columns = ["Date", "Daily_Total"]

df = df.merge(daily_total, on="Date", how="left")

# -----------------------------
# SAVE UPDATED DATA
# -----------------------------
df.to_csv("data/featured_expenses.csv", index=False)

print("Feature Engineering Completed!")
print(df.head())