from datetime import datetime
from storage.file_storage import load_expenses
from collections import defaultdict


def show_summary():

    expenses = load_expenses()

    if not expenses:
        print("No expenses to summarize.\n")
        return

    # -------- DAILY SUMMARY --------

    user_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if user_date == "":
        user_date = datetime.today().date().isoformat()

    filtered = []

    for exp in expenses:
        exp_date = exp["datetime"].split("T")[0]

        if exp_date == user_date:
            filtered.append(exp)

    if filtered:

        total = sum(exp["amount"] for exp in filtered)
        average = total / len(filtered)

        category_total = defaultdict(float)

        for exp in filtered:
            category_total[exp["category"]] += exp["amount"]

        categories = set(exp["category"] for exp in filtered)

        print(f"\nExpense Summary for {user_date}")
        print(f"Total Spent: {total}")
        print(f"Total Expenses: {len(filtered)}")
        print(f"Average Expense: {average:.2f}")

        print("\nExpenses with Category:")
        for exp in filtered:
            print(f"{exp['category']} : {exp['amount']}")

        print("\nSpending by Category:")
        for cat, amt in category_total.items():
            print(f"{cat}: {amt}")

        print("\nCategories used:", ", ".join(categories))

        user_category = input("\nEnter category to see total and average (or press Enter to skip): ")

        if user_category:

            category_filtered = [exp for exp in filtered if exp["category"] == user_category]

            if not category_filtered:
                print("No expenses found for this category.")
            else:
                cat_total = sum(exp["amount"] for exp in category_filtered)
                cat_avg = cat_total / len(category_filtered)

                print(f"\nTotal for {user_category}: {cat_total}")
                print(f"Average for {user_category}: {cat_avg:.2f}")

    else:
        print("No expenses found for that date.")

    # -------- MONTHLY SUMMARY --------##

    print("\n------ Monthly Summary ------")

    user_month = input("Enter month (YYYY-MM) or press Enter to skip: ")

    if user_month:

        monthly_total = 0
        monthly_count = 0

        for exp in expenses:

            month = exp["datetime"][:7]

            if month == user_month:
                monthly_total += exp["amount"]
                monthly_count += 1

        if monthly_count == 0:
            print("No expenses found for this month.")
        else:
            monthly_avg = monthly_total / monthly_count

            print(f"\nMonthly Summary for {user_month}")
            print(f"Total Expenses: {monthly_count}")
            print(f"Total Spent: {monthly_total}")
            print(f"Average Spending: {monthly_avg:.2f}")