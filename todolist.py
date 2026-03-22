
tasks = []

def show_task():
    if len(tasks) == 0:
        print("NO tak in the list")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n----------To-Do Menu--------")
    print("1.Add Task")
    print("2.view Task")
    print("3.remove task")
    print("4.Exit")

    
    
    choice = input("Enter yor choice between(1-4):")

    if choice == "1":
        task = input("Enter Task:")
        tasks.append(task)
        print("Task added succesfully")

    elif choice == "2":
        show_task()

    elif choice == "3":
        show_task()
        try:
            task_num = int(input("Enter task number to remove:"))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Enter valid task number")
        except ValueError:
            print("Please enter a valid value")
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice,Please try again!")

