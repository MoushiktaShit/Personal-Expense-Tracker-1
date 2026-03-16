import json

FILE_NAME = "data/expenses.json"

def load_expenses():
    try:
        with open("data/expenses.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_expenses(expenses):
    print("Saving to:", "data/expenses.json")
    print("Saving:", expenses)

    with open("data/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)