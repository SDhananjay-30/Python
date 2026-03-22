
def show_balance():
    print(f"Your Total Balance:{balance}")

def deposite():
    amount = float(input("Enter amount to be deposited:"))

    if amount < 0:
        print("Enter a Valid amount..")
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be Withdraw:"))

    if amount < 0:
        print("Enter a Valid amount..")
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("-----Banking Program------")
    print("1.Display Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter Choice between (1-4):")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance+=deposite()
    elif choice == "3":
        balance-=withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Enter a Valid Choice.........")
print("Thank you...!Have a nice Day.....")