import json

FILE_NAME = "data/expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_expenses(expenses):
    print("Saving:", expenses)
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)