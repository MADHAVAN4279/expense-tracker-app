import pandas as pd

# Example DataFrame of expenses
data = {
    'Description': ['Groceries', 'Transport', 'Bills'],
    'Amount': [50, 20, 100],
    'Category': ['Food', 'Transport', 'Bills'],
    'Date': ['2021-10-01', '2021-10-02', '2021-10-03']
}

df = pd.DataFrame(data)

# Function to add a new expense
def add_expense(description, amount, category, date):
    global df
    new_expense = pd.DataFrame({
        'Description': [description],
        'Amount': [amount],
        'Category': [category],
        'Date': [date]
    })
    df = pd.concat([df, new_expense], ignore_index=True)
    return df
