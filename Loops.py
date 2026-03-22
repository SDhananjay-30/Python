# WHihle Loop 

# n = int(input("Enter the value of n:"))

# i = 1

# while (i<=10) :
#     print(n*i)
#     i+=1

# i = 1

# while (i <=10) :
#     if(i%6 == 0) :
#         break
#     print(i)
#     i += 1

# print("Outside the loop....")

# i = 1

# while(i <= 10) :
#     if(i%5 == 0) :
#         i += 1
#         continue
        
#     print(i)
#     i += 1

# Temperature conversion
# C = float(input("Enter the temp. in celcius:"))

# temp_type = input("Enter the converting temp.")

# match temp_type:
#     case "Faranite":
#         F=(C*9/5)+32
#         print("Temp. in faranite :",F)
#     case "Kelvin":
#         K = (C+273.15)
#         print("temp. in kelvin:",K)
#     case _:
#         print("Enter valid Data")

#Weight Conversion

W = input("Enter the weight:")
temp = input("Enter the converting weight:")

if(temp == "Gram"):
    G = int(W*1000)
    print("Weight in gram :",G)
elif (temp == "Miligram") :
    M = W*1,000,000
    print("WWeight in miligram:",M)
elif(temp == "Pound") :
    P = W*2.20462
    print("Weight in pound :",P)
else:
    print("Enter valid Data")

    