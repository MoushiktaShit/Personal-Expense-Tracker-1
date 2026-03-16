from storage.file_storage import load_expenses, save_expenses
from datetime import datetime

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

    user_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    now = datetime.now()

    if user_date == "":
        expense_datetime = now
    else:
        current_time = now.strftime("%H:%M:%S")
        datetime_combined = user_date + " " + current_time
        expense_datetime = datetime.strptime(datetime_combined, "%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "datetime": expense_datetime.isoformat()
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully\n")

from storage.file_storage import load_expenses
from datetime import datetime

def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    user_date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")

    if user_date == "":
        user_date = datetime.today().date().isoformat()

    filtered = []

    for exp in expenses:
        exp_date = exp["datetime"].split("T")[0]

        if exp_date == user_date:
            filtered.append(exp)

    if not filtered:
        print("No expenses in the filtered date.\n")
        return

    print(f"\nExpenses for {user_date}:\n")

    for i, exp in enumerate(filtered, start=1):
        print(
            f"{i}. Amount: {exp['amount']} | "
            f"Category: {exp['category']} | "
            f"Datetime: {exp['datetime']}"
        )

    print()
    
def delete_expense():

    expenses = load_expenses()

    if not expenses:
        print("No expenses to delete\n")
        return
    user_date =input("Enter date (YYYY-MM-DD):")
    filtered = [exp for exp in expenses if exp["datetime"].startswith(user_date)]
    if not filtered:
        print("No expenses found for the given date.\n")
        return

    print(f"\nExpenses for {user_date}:\n")

    for i, exp in enumerate(filtered, start=1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['datetime']}")

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(filtered):
        expense_to_delete = filtered[index]
        expenses.remove(expense_to_delete)
        save_expenses(expenses)
        print("Expense deleted\n")
    else:
        print("Invalid index\n")