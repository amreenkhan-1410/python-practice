import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Personal Expense Tracker", layout="centered")

st.title("💰 Personal Expense Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state["expenses"] = pd.DataFrame(columns=["Date", "Category", "Amount"])

# Input form
with st.form("expense_form"):
    exp_date = st.date_input("Select Date", date.today())
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_expense = pd.DataFrame(
            {"Date": [pd.to_datetime(exp_date)], "Category": [category], "Amount": [amount]}
        )
        st.session_state["expenses"] = pd.concat(
            [st.session_state["expenses"], new_expense], ignore_index=True
        )
        st.success("Expense added!")

# Ensure Date column is datetime
if not st.session_state["expenses"].empty:
    st.session_state["expenses"]["Date"] = pd.to_datetime(st.session_state["expenses"]["Date"])

# Show table
st.subheader("📊 Expense Records")
st.dataframe(st.session_state["expenses"], use_container_width=True)

# Monthly summary
if not st.session_state["expenses"].empty:
    st.subheader("📅 Monthly Summary")
    st.session_state["expenses"]["Month"] = st.session_state["expenses"]["Date"].dt.to_period("M")

    monthly_summary = st.session_state["expenses"].groupby("Month")["Amount"].sum().reset_index()
    st.bar_chart(monthly_summary.set_index("Month"))

    # Category-wise distribution
    st.subheader("📂 Category Breakdown")
    category_summary = st.session_state["expenses"].groupby("Category")["Amount"].sum().reset_index()

    st.bar_chart(category_summary.set_index("Category"))
