def view_expenses(expenses):
    if not expenses:
        print("There are no expenses currently added. To add an expense select option 2")
        return
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. Name: {expense['name']}\n   Price: ${expense['amount']:.2f}\n")


def add_expense(expenses):
    new_expense = {}
    new_expense["name"] = input("What's the name of the expense? ")
    new_expense["amount"] = float(input("How much was the expense? "))
    expenses.append(new_expense)


def calculate_total(expenses):
    total_expense = 0
    items = len(expenses)
    if items == 0:
        print("There are no expenses.")
        return
    for expense in expenses:
        total_expense += expense["amount"]
    print(
        f"The total amount of your {items} expenses is {total_expense:.2f} dollars.")


def calculate_average(expenses):
    average_expense = 0
    items = len(expenses)
    if items == 0:
        print("There are no expenses.")
        return
    for expense in expenses:
        average_expense += expense["amount"]
    average_expense = average_expense / items
    print(
        f"The average amount of your {items} expenses is {average_expense:.2f} dollars.")


expenses = []

while True:
    print("Expense Calculator\n")
    print("1. View All Expenses\n2. Add Expense\n3. Calculate Total Expenses\n4. Total Average Expenses\n5. Quit\n")
    user_input = input("Please select an option from the menu: ")
    if user_input == "1":
        view_expenses(expenses)
    elif user_input == "2":
        add_expense(expenses)
    elif user_input == "3":
        calculate_total(expenses)
    elif user_input == "4":
        calculate_average(expenses)
    elif user_input == "5":
        break
    else:
        print("Invalid menu option!")
