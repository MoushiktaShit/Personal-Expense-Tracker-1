from storage.file_storage import load_expenses, save_expenses
from datetime import date

def add_expense():
    expenses = load_expenses()

    amount = float(input("Enter amount: "))

    print("Select Category:")
    print("1. Food")
    print("2. Transport")
    print("3. Other")

    choice = input("Enter category number: ")

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    else:
        category = "Other"

    user_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if user_date == "":
        user_date = str(date.today())

    expense = {
        "amount": amount,
        "category": category,
        "date": user_date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully\n")

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found")
        return

    for i, exp in enumerate(expenses, start=1):
         print(f"{i}. {exp['amount']} | {exp['category']} | {exp['date']}")


def delete_expense():
    expenses = load_expenses()

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
        print("Expense deleted")
    else:
        print("Invalid index")