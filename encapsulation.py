
# class Bank():
#     def __init__(self,Account,balance):
#         self.Account = Account
#         self.__balance = balance
    
#     def get__balance(self):
#         print(f"user has {self.Account} account type")
#         return self.__balance
    
#     def set_balance(self,new_balance):
#         self.__balance = new_balance

# e = Bank("Current",50000)
# print(f"Account Balance :{e.get__balance()}")
# e.set_balance(100000)       

# class Teacher():
#     def __init__(self,salary):
#         self.salary = salary
    
# class Student:
#     def __init__(self,gpa):
#         self.gpa = gpa

# class TA(Teacher,Student):
#     def __init__(self,salary,gpa,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name = name

# ta1 = TA(15_000,9.8,"Om")
# print(ta1.name,ta1.gpa,ta1.salary)
\


# class Person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"{self.name} has age:{self.age}")

# class Student(Person):
#     def __init__(self,marks,name,age):
#         self.marks = marks
#         super().__init__(name,age)

#     def display_marks(self):
#         print(f"{self.name} has age:{self.age},has got marks:{self.marks}")

# t1 = Student(90,"Om",20)
# t1.display_marks()

class BankAccount():
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposite(self,deposite_value):
        self.deposite_value = deposite_value
        print(f"Total current balance:{self.balance+deposite_value}")

    def withdraw(self,withdraw_val):
        self.withdraw_val = withdraw_val
        print(f"withdraw Value:{withdraw_val}")
        print(f"Total current Balance:{self.balance-withdraw_val}")

u1 =BankAccount(101,"Yash",10000)
u1.deposite(500)
u1.withdraw(100)
        
        



        