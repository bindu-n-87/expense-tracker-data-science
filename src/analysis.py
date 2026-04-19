import pandas as pd

# -----------------------------
# LOAD FEATURED DATA
# -----------------------------
df = pd.read_csv("data/featured_expenses.csv")

print("🔹 Data Preview:")
print(df.head())

# -----------------------------
# TOTAL SPENDING
# -----------------------------
total_spending = df["Amount"].sum()
print("\nTotal Spending:", total_spending)

# -----------------------------
# CATEGORY ANALYSIS
# -----------------------------
category_analysis = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

print("\nCategory-wise Spending:")
print(category_analysis)

# -----------------------------
# ESSENTIAL VS NON-ESSENTIAL
# -----------------------------
expense_type_analysis = df.groupby("Expense_Type")["Amount"].sum()

print("\nEssential vs Non-Essential:")
print(expense_type_analysis)

# -----------------------------
# WEEKEND VS WEEKDAY
# -----------------------------
weekend_analysis = df.groupby("Is_Weekend")["Amount"].sum()

print("\nWeekend vs Weekday Spending:")
print(weekend_analysis)

# -----------------------------
# SPENDING LEVEL DISTRIBUTION
# -----------------------------
spending_level_count = df["Spending_Level"].value_counts()

print("\nSpending Level Distribution:")
print(spending_level_count)

# -----------------------------
# MONTHLY ANALYSIS
# -----------------------------
monthly_analysis = df.groupby("Month_Name")["Amount"].sum().sort_values()

print("\nMonthly Spending:")
print(monthly_analysis)

# -----------------------------
# TOP 5 HIGHEST EXPENSES
# -----------------------------
top_expenses = df.sort_values(by="Amount", ascending=False).head(5)

print("\nTop 5 Highest Expenses:")
print(top_expenses)

# -----------------------------
# INSIGHTS GENERATION
# -----------------------------
print("\nINSIGHTS:")

# Insight 1
top_category = category_analysis.idxmax()
print(f"Highest spending category: {top_category}")

# Insight 2
if expense_type_analysis["Non-Essential"] > expense_type_analysis["Essential"]:
    print("User spends more on NON-ESSENTIAL items")
else:
    print("User spends more on ESSENTIAL items")

# Insight 3
if weekend_analysis[True] > weekend_analysis[False]:
    print("Higher spending on WEEKENDS")
else:
    print("Higher spending on WEEKDAYS")

# Insight 4
top_month = monthly_analysis.idxmax()
print(f"Highest spending month: {top_month}")