import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/featured_expenses.csv")

# Style setup
sns.set(style="whitegrid")

category = df.groupby("Category")["Amount"].sum().sort_values()

plt.figure(figsize=(10,6))
category.plot(kind='barh')
plt.title("Category-wise Spending")
plt.xlabel("Amount")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig("outputs/category_horizontal.png")
plt.close()

monthly = df.groupby("Month_Name")["Amount"].sum()

plt.figure(figsize=(10,6))
monthly.plot(marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Total Spending")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/monthly_trend_final.png")
plt.close()

expense_type = df.groupby("Expense_Type")["Amount"].sum()

plt.figure(figsize=(6,6))
expense_type.plot(kind='pie', autopct='%1.1f%%')
plt.title("Essential vs Non-Essential Spending")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/expense_type_pie.png")
plt.close()

weekend = df.groupby("Is_Weekend")["Amount"].sum()

plt.figure(figsize=(6,5))
weekend.plot(kind='bar')
plt.title("Weekend vs Weekday Spending")
plt.xlabel("Is Weekend")
plt.ylabel("Total Spending")
plt.tight_layout()
plt.savefig("outputs/weekend_spending.png")
plt.close()

spending_level = df["Spending_Level"].value_counts()

plt.figure(figsize=(6,5))
spending_level.plot(kind='bar')
plt.title("Spending Level Distribution")
plt.xlabel("Level")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/spending_levels.png")
plt.close()

plt.figure(figsize=(8,5))
sns.boxplot(x=df["Amount"])
plt.title("Outlier Detection (Expenses)")
plt.tight_layout()
plt.savefig("outputs/outliers_boxplot.png")
plt.close()

print("All visualizations created successfully!")
