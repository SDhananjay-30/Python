# class Student():
#     def __init__(self,name,cgpa):
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa

# std1 = Student("Rahul",9.8)
# std2 = Student("OM",9.5)

# print(f"{std1.name} has got cgpa {std1.get_cgpa()}")
# print(f"{std2.name} has got cgpa {std2.get_cgpa()}")

# # class Student():
# #     def __init__(self):
# #         print("Constructor is called")

# # std1 = Student()

# class Student():
#     college_name = "Sinhgad College of Engineering"

#     def __init__(self,name,iD):
#         self.name = name
#         self.iD = iD
    
# stu1 = Student("jay","30B016")
# print(f"{stu1.name} has roll number:{stu1.iD}")
# print(f"My College name is :{Student.college_name}")

class Student():
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

    def get_info(self):
        print(f"Name:{std1.name},Marks:{std1.gpa}")        

std1 = Student("Om",9.8)

std1.get_info()
