from storage.file_storage import load_expenses

def show_summary():
    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.\n")
        return

    total = sum(exp["amount"] for exp in expenses)

    category_total = {}

    for exp in expenses:
        cat = exp["category"]
        category_total[cat] = category_total.get(cat, 0) + exp["amount"]

    average = total / len(expenses)

    print("\nExpense Summary\n")
    print(f"Total Spent: {total}")

    print("\nSpending by Category:")
    for cat, amt in category_total.items():
        print(f"{cat}: {amt}")

    print(f"\nAverage Expense: {average:.2f}\n")