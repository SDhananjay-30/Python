def view_bal():
    print(f"Total Balance:{balance}")

def add_income():
    amount = float(input("Enter amount to add:"))

    if amount < 0:
        print("Enter a valid amount:")
    else:
        return amount
def add_expense():
    amount = float(input("Enter expense amount:"))
    category = input("Enter Category(food/travel/bills):")
    description = input("Enter Description:")
    Expence.append({"amount":amount,"category":category,"Description":description})
    print("Expense Added!")

def view_expense():
    print(f"Expenses:{Expence}\n")

Expence = []
balance = 0
is_running = True

while is_running:
    print("Welcome to Expense Manager")
    print("1.view Balance")
    print("2.Add Income")
    print("3.Add Expense")
    print("4.View Expenses")
    print("5.Exit")

    choice = input("Enter Task to be perform:")


    if choice == "1":
        view_bal()
    elif choice == "2":
        balance+=add_income()
    elif choice == "3":
        add_expense()
    elif choice == "4":
        view_expense()
    elif choice == "5":
        is_running = False
    else:
        print("Enter a Valid Choice")
