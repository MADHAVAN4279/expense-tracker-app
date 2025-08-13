import streamlit as st
import pandas as pd
import joblib
from expense_tracker_logic import add_expense  # Import the function from the logic file

# Initialize the DataFrame (same as before)
df = pd.DataFrame({
    'Description': ['Groceries', 'Transport', 'Bills'],
    'Amount': [50, 20, 100],
    'Category': ['Food', 'Transport', 'Bills'],
    'Date': ['2021-10-01', '2021-10-02', '2021-10-03']
})

# Display Title
st.title("Expense Tracker")

# Add Expense Form
with st.form(key='add_expense_form'):
    description = st.text_input('Description')
    amount = st.number_input('Amount', min_value=0)
    category = st.selectbox('Category', ['Food', 'Transport', 'Bills', 'Entertainment'])
    date = st.date_input('Date')

    submit_button = st.form_submit_button(label='Add Expense')

    if submit_button:
        # Add expense using the function from the logic file
        df = add_expense(description, amount, category, date)
        st.success("Expense Added Successfully!")

# Show Expenses Table
st.subheader("Expenses")
st.write(df)
