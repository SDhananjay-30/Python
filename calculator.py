
while True:
    A = int(input("Enter value of A:"))
    B = int(input("Enter Value of B:"))


    print("\n------Calculator Menu------")
    print("1.Adddition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = input("Enter Choice Between(1-5):")

    if choice == "1":
        print(f"Addition of two numbers:{A+B}")
        print("Addition perform Succesfully")
    elif choice == "2":
        print(f"Substraction :{A-B}")
    elif choice == "3":
        print(f"Multiplication:{A*B}")
    elif choice == "4":
        print(f"Division:{A/B}")
    elif choice == "5":
        print("Good bye!")
        break
    else:
        print("Enter Valid Choice...........")