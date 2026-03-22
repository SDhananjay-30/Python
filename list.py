

# marks = [80,50,60,90,70,30]
# # print(marks)
# # print(len(marks))
# print(marks[5])

# marks[3] = 100
# print(marks)

# marks.append(75)
# print(marks)

# marks.insert(5,58)
# print(marks)

# marks.sort()
# print(marks)

# marks.reverse()
# print(marks)

# tup = (2,5,8,7,3,10,5,2,5)

# print(tup.count(5))

# dict = {
#     "name" : "Om",
#     "Subject" : ["Math","English"],
#     "Score" : 95
# }

# print(dict["name"])
# print(dict["Score"])
# print(dict["Subject"])
# print(dict.items())

# info = [
#     ("Alice","English"),
#     ("Om","Science"),
#     ("Yash","Science"),
#     ("Shiva","English"),
#     ("Bob","Math"),
#     ("Alice","English"),
#     ("Charlie","English")
# ]


# for name,course in info:
#     if(course == "English"):
#         print(name)

# Word = input("Enter word:")

# print(Word[::-1])

# if(Word == Word[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# nums = [5,10,4,6,8]

# average = sum(nums)/len(nums)
# print("Average of nums:",average)

# nums1 = []

# n1 = int(input("How many numbers:"))

# for i in range(n1):
#     num = int(input("Enter nnumber:"))
#     nums1.append(num)
# print("List one:",nums1)

# num2 =[]

# n2 = int(input("how many numbers:"))

# for i in range(n2):
#     num = int(input("Enter numbers:"))
#     num2.append(num)
# print("List Two:",num2)

# merged = [nums1+num2]

# print(merged)

# merged.sort()
# print(merged)

# tuple1 =  tuple(map(int, input("Enter elements: ").split(",")))
# print(tuple1)

# eventup = []
# oddtup = []

# for i in tuple1:
#     if(i % 2 == 0):
#         eventup.append(i)
#     else:
#         oddtup.append(i)

# new_eventup = tuple(eventup)
# new_oddtup = tuple(oddtup)
# print("Even tuple:",new_eventup)
# print("Odd Tuple:",new_oddtup)
# --------------------------------------------

# info = {}

# while True:
#     print("------Menu-------")
#     print("A-Add a student")
#     print("B-Update Marks")
#     print("C-Search for Student")
#     print("D-Display all student and Marks")
#     print("E-Exit")

#     choice = input("Enter choice:")
    
#     if (choice == 'A'):
#         name = input("Enter Student name:")
#         marks = input("Enter marks:")
#         info[name] = marks
#         print("Student added Succesfully")
    
#     elif(choice == 'B'):
#         name = input("Enter student name to update: ")
#         if name in info:
#             marks = int(input("Enter new marks: "))
#             info[name] = marks
#             print("Marks updated.")
#         else:
#             print("Student not found.")
#     elif choice == 'C':
#         name = input("Enter student name to search: ")
#         if name in info:
#             print(name, "marks =", info[name])
#         else:
#             print("Student not found.")

#     # 4️⃣ Display All
#     elif choice == 'D':
#         if info:
#             print("\nStudent Records:")
#             for name, marks in info.items():
#                 print(name, ":", marks)
#         else:
#             print("Dictionary is empty.")

#     # Exit
#     elif choice == 'E':
#         print("Program ended.")
#         break

#     else:
#         print("Invalid choice. Try again.")
# ------------------------------------------------------


words = {
    "Banana",
    "Mango",
    "Apple",
    "Kiwi",
    "Papaya",
}

for key in words:
    print(key,"length=",len(key))
