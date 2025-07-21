import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# Set page configuration
st.set_page_config(page_title="Expense Tracker", layout="wide")

# Load expenses from CSV or initialize empty DataFrame
def load_expenses():
    try:
        return pd.read_csv("expenses.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Description", "Amount", "Category", "Date"])

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = load_expenses()

# Sidebar for filters
st.sidebar.header("Filter Expenses")
category_filter = st.sidebar.multiselect(
    "Select Categories:", 
    options=["Food", "Travel", "Shopping", "Bills", "Other"],
    default=["Food", "Travel", "Shopping", "Bills", "Other"]
)
min_amount = st.sidebar.number_input("Minimum Amount:", min_value=0.0, value=0.0, step=10.0)

# Filter expenses
filtered_df = st.session_state.expenses[
    (st.session_state.expenses["Category"].isin(category_filter)) &
    (st.session_state.expenses["Amount"] >= min_amount)
]

# Main content
st.title("Streamlit Expense Tracker")

# Form for adding expenses
st.subheader("Add New Expense")
with st.form(key="expense_form"):
    description = st.text_input("Description:", placeholder="e.g., Coffee")
    amount = st.number_input("Amount ($):", min_value=0.0, step=0.01)
    category = st.selectbox("Category:", ["Food", "Travel", "Shopping", "Bills", "Other"])
    expense_date = st.date_input("Date:", value=date.today())
    submit_button = st.form_submit_button("Add Expense")

    if submit_button:
        if description and amount > 0:
            new_expense = pd.DataFrame({
                "Description": [description],
                "Amount": [amount],
                "Category": [category],
                "Date": [expense_date]
            })
            st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
            st.session_state.expenses.to_csv("expenses.csv", index=False)
            st.success("Expense added and saved to CSV!")
        else:
            st.error("Please provide a description and a positive amount.")

# Layout with columns
col1, col2 = st.columns([3, 2])

# Column 1: Filtered expenses table and summary
with col1:
    st.subheader("Expense List")
    if not filtered_df.empty:
        st.write(f"Showing {len(filtered_df)} expenses:")
        st.dataframe(filtered_df)
        st.metric("Total Expenses", f"${filtered_df['Amount'].sum():.2f}")
    else:
        st.warning("No expenses match the current filters or no expenses added yet.")

# Column 2: Pie chart
if not filtered_df.empty:
    with col2:
        st.subheader("Expenses by Category")
        category_sums = filtered_df.groupby("Category")["Amount"].sum().reset_index()
        fig = px.pie(
            category_sums,
            names="Category",
            values="Amount",
            title="Expense Distribution",
            color_discrete_sequence=px.colors.qualitative.Plotly
        )
        fig.update_traces(textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

# Footer note
st.write("**Tip**: Add expenses using the form and use sidebar filters to explore your data!")
