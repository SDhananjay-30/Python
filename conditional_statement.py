# color = input("Enter the color:")

# if color == "Green":
#     print("You can go")
# elif color == "Red":
#     print("Stop")
# elif color == "Yellow":
#     print("Look")
# else:
#     print("Wrong Color")



# age = int(input("Enter your age:"))
# if (age==1 and age <=13) :
#     print("Child")
# elif (age>=13 and age<=18 ) :
#     print("Teenage")
# elif (age >= 18) :
#     print("Adult")
# else :
#     print("Enter Valid Data")



# n = int(input("Enter num:"))
# if ( n%2 == 0) :
#     print("N is  even")
# else :
#     print("N is not odd")



# username = input("Enter Username:")
# password = input("Enter password:")
# if(username == "admin" and password == "pass") :
#     print("LOGIN SUCCESSFULLY")
# else :
#     if(username != "admin") :
#         print("Wrong Username")
#     elif(password != "pass") :
#         print("Wrong Password")
    
color = input("Enter the color:")

match color :
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red" :
        print("Stop")
    case _ :
        print("Enter valid data")