# Personal Budget Tracker
# A simple command-line app to track income and expenses with visualization

import matplotlib.pyplot as plt
from datetime import datetime

# Initialize data structures
budget = {
    "income": 0.0,
    "expenses": [],
    "categories": {}
}

def add_income():
    """Add income to the budget."""
    try:
        amount = float(input("Enter income amount: $"))
        if amount < 0:
            print("Income cannot be negative!")
            return
        budget["income"] += amount
        print(f"Added ${amount:.2f} to income. Total income: ${budget['income']:.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")

def add_expense():
    """Add a single expense with category and description."""
    try:
        amount = float(input("Enter expense amount: $"))
        if amount < 0:
            print("Expense cannot be negative!")
            return
        category = input("Enter expense category (e.g., Food, Rent, Entertainment): ").capitalize()
        description = input("Enter expense description: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        expense = {"amount": amount, "category": category, "description": description, "date": date}
        budget["expenses"].append(expense)
        
        # Update category totals
        if category in budget["categories"]:
            budget["categories"][category] += amount
        else:
            budget["categories"][category] = amount
            
        print(f"Added expense: ${amount:.2f} for {description} ({category})")
    except ValueError:
        print("Invalid input! Please enter a number for the amount.")

def add_multiple_expenses():
    """Add multiple expenses in one session."""
    print("\n=== Add Multiple Expenses ===")
    print("Enter expenses one by one. Type 'done' when finished.")
    
    while True:
        user_input = input("\nEnter expense amount (or 'done' to finish): $")
        if user_input.lower() == 'done':
            print("Finished adding expenses.")
            break
        try:
            amount = float(user_input)
            if amount < 0:
                print("Expense cannot be negative!")
                continue
            category = input("Enter expense category (e.g., Food, Rent, Entertainment): ").capitalize()
            description = input("Enter expense description: ")
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            expense = {"amount": amount, "category": category, "description": description, "date": date}
            budget["expenses"].append(expense)
            
            # Update category totals
            if category in budget["categories"]:
                budget["categories"][category] += amount
            else:
                budget["categories"][category] = amount
                
            print(f"Added expense: ${amount:.2f} for {description} ({category})")
        except ValueError:
            print("Invalid input! Please enter a number for the amount or 'done' to finish.")

def view_summary():
    """Display budget summary."""
    total_expenses = sum(expense["amount"] for expense in budget["expenses"])
    balance = budget["income"] - total_expenses
    
    print("\n=== Budget Summary ===")
    print(f"Total Income: ${budget['income']:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    
    if budget["categories"]:
        print("\nExpenses by Category:")
        for category, amount in budget["categories"].items():
            print(f"{category}: ${amount:.2f}")

def plot_expenses():
    """Plot a bar chart of expenses by category."""
    if not budget["categories"]:
        print("No expenses to plot!")
        return
    
    categories = list(budget["categories"].keys())
    amounts = list(budget["categories"].values())
    
    plt.bar(categories, amounts)
    plt.title("Expenses by Category")
    plt.xlabel("Categories")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to run the budget tracker."""
    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Income")
        print("2. Add Single Expense")
        print("3. Add Multiple Expenses")
        print("4. View Summary")
        print("5. Plot Expenses")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            add_multiple_expenses()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            plot_expenses()
        elif choice == "6":
            print("Thank you for using the Budget Tracker!")
            break
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
