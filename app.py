import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Expense Tracker Dashboard", layout="wide")

st.title("Expense Tracker Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/featured_expenses.csv")

df = load_data()

st.sidebar.header("Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

month_filter = st.sidebar.multiselect(
    "Month",
    options=df["Month_Name"].unique(),
    default=df["Month_Name"].unique()
)

budget = st.sidebar.number_input(
    "Monthly Budget",
    min_value=1000,
    value=20000,
    step=500
)

filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Month_Name"].isin(month_filter))
]

total_spent = filtered_df["Amount"].sum()
avg_spent = filtered_df["Amount"].mean()
max_spent = filtered_df["Amount"].max()

budget_used = (total_spent / budget) * 100
savings = budget - total_spent

col1, col2, col3 = st.columns(3)

col1.metric("Total Spending", f"{total_spent:,.0f}")
col2.metric("Average Expense", f"{avg_spent:,.0f}")
col3.metric("Max Expense", f"{max_spent:,.0f}")

st.divider()

st.subheader("Budget Status")

st.write(f"Budget Used: {budget_used:.2f}%")

if budget_used > 100:
    st.error("Budget Exceeded")
elif budget_used > 80:
    st.warning("Near Budget Limit")
else:
    st.success("Within Budget")

if savings >= 0:
    st.success(f"Savings: {savings:,.0f}")
else:
    st.error(f"Overspending: {abs(savings):,.0f}")

st.divider()

FIGSIZE = (4.5, 3.2)

st.subheader("Analytics Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Category-wise Spending")

    category_data = filtered_df.groupby("Category")["Amount"].sum()

    fig1, ax1 = plt.subplots(figsize=FIGSIZE)
    category_data.plot(kind="bar", ax=ax1)
    ax1.set_xlabel("")
    ax1.set_ylabel("")
    ax1.tick_params(axis="x", rotation=45)

    st.pyplot(fig1, use_container_width=True)


with col2:
    st.markdown("Monthly Spending Trend")

    monthly_data = filtered_df.groupby("Month_Name")["Amount"].sum()

    fig2, ax2 = plt.subplots(figsize=FIGSIZE)
    monthly_data.plot(marker="o", ax=ax2)
    ax2.set_xlabel("")
    ax2.set_ylabel("")

    st.pyplot(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("Expense Breakdown")

    expense_type = filtered_df.groupby("Expense_Type")["Amount"].sum()

    fig3, ax3 = plt.subplots(figsize=FIGSIZE)
    expense_type.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
    ax3.set_ylabel("")

    st.pyplot(fig3, use_container_width=True)


with col4:
    st.markdown("High Expense Analysis")

    threshold = filtered_df["Amount"].quantile(0.90)
    high_spend = filtered_df[filtered_df["Amount"] > threshold]

    fig4, ax4 = plt.subplots(figsize=FIGSIZE)

    if len(high_spend) > 0:
        high_spend.groupby("Category")["Amount"].sum().plot(kind="bar", ax=ax4)
    else:
        ax4.text(0.3, 0.5, "No High Expenses", fontsize=12)

    st.pyplot(fig4, use_container_width=True)

st.divider()

st.subheader("Filtered Data")
st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Report",
    data=csv,
    file_name="expense_report.csv",
    mime="text/csv"
)
