import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Define a function to load the expense data
def load_expenses(filename='expenses.csv'):
    try:
        expenses = pd.read_csv(filename)
    except FileNotFoundError:
        # If no file exists, create a new DataFrame with the necessary columns
        expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount'])
    return expenses

# Function to log a new expense
def log_expense(expenses, category, amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp for expense
    new_expense = pd.DataFrame([[date, category, amount]], columns=expenses.columns)
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    return expenses

# Function to save the data to a CSV file
def save_expenses(expenses, filename='expenses.csv'):
    expenses.to_csv(filename, index=False)

# Function to analyze the expenses
def analyze_expenses(expenses):
    total_spent = expenses['Amount'].sum()
    print(f"Total Expenses: ₹{total_spent:.2f}")
    category_spending = expenses.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    print("\nSpending by Category:")
    print(category_spending)
    return category_spending

# Function to visualize the spending trends
def visualize_expenses(expenses):
    expenses['Date'] = pd.to_datetime(expenses['Date'])

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(expenses['Date'], expenses['Amount'], marker='o', color='b', label='Expenses')

#    Adding labels and title
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Expenses Over Time')
    plt.legend()

    # Show the plot
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust the layout to prevent overlapping labels
    plt.show()
    
    # Plotting category-wise spending over time
    plt.figure(figsize=(10, 6))
    expenses.groupby([expenses['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().unstack().plot(kind='bar', figsize=(12, 7))
    plt.title('Monthly Spending Trends by Category')
    plt.xlabel('Month')
    plt.ylabel('Amount (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to interact with the user
def main():
    expenses = load_expenses()  # Load previous data if available
    while True:
        print("\nExpense Tracker")
        print("1. Log Expense")
        print("2. Analyze Expenses")
        print("3. Visualize Spending Trends")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            category = input("Enter the category (e.g., Food, Transportation, etc.): ")
            amount = float(input("Enter the amount spent: ₹"))
            expenses = log_expense(expenses, category, amount)
            save_expenses(expenses)
            print("Expense logged successfully!")
        
        elif choice == '2':
            analyze_expenses(expenses)
        
        elif choice == '3':
            visualize_expenses(expenses)
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
