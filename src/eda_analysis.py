import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_expenses.csv")

print("🔹 Data Preview:")
print(df.head())

print("\n🔹 Summary Statistics:")
print(df["Amount"].describe())

category_spending = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

print("\n🔹 Category-wise Spending:")
print(category_spending)

monthly_spending = df.groupby("Month")["Amount"].sum()

print("\n🔹 Monthly Spending:")
print(monthly_spending)

payment_analysis = df["Payment_Method"].value_counts()

print("\n🔹 Payment Method Usage:")
print(payment_analysis)

top_days = df.sort_values(by="Amount", ascending=False).head(5)

print("\n🔹 Top 5 Expenses:")
print(top_days)


# Style
sns.set(style="whitegrid")

# 1. Category Bar Chart
plt.figure(figsize=(8,5))
category_spending.plot(kind='bar')
plt.title("Category-wise Spending")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/category_bar.png")
plt.close()

# 2. Monthly Trend
plt.figure(figsize=(8,5))
monthly_spending.plot(marker='o')
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Total Amount")
plt.grid()
plt.tight_layout()
plt.savefig("outputs/monthly_trend.png")
plt.close()

# 3. Payment Method Pie Chart
plt.figure(figsize=(6,6))
payment_analysis.plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/payment_pie.png")
plt.close()

# 4. Box Plot (Outliers)
plt.figure(figsize=(8,5))
sns.boxplot(x=df["Amount"])
plt.title("Expense Distribution (Outliers Detection)")
plt.tight_layout()
plt.savefig("outputs/boxplot.png")
plt.close()

print("\nEDA Completed! Charts saved in outputs/")
