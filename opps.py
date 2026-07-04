# # # # the concept of object is similar to real word senario 
# # # # Before creating an object we have to create a class

# # # #think of a real school 
# # #   #1 . first we have to make class 
# # #   #2 . and after that we arrange student and to seat them that is called an object.
# # #   #Class is a blueprint for creating an object
  
# # # class Student: 
# # #     college_Name = "Silicon Institute of technology" #
# # #     def __init__(self,student_name,student_rollno):
# # #         self.name = student_name # instance attribute
# # #         self.roll = student_rollno #instance attribute
    
# # # classRoom = []

# # # for i in range(10):
# # #     print(f"\n--- Entering details for Student {i + 1} ---")
# # #     entered_Name  = input("Please enter the student name: ")
# # #     entered_RollNo = input("Please enter student Roll number: ")
    
# # #     new_student = Student(entered_Name,entered_RollNo)
# # #     classRoom.append(new_student)

# # # print("ALL STUDENT HAVE BEEN SAVED")

# # # print("\n--- Classroom Roster ---")

# # # # Go through the list one by one
# # # for student in classRoom:
# # #     # Use the dot (.) to look inside the object and grab the data
# # #     print(f"Name: {student.name} | Roll No: {student.roll}")

# # #STATIC METHOD
# # # method is the function written inside the class

# # class Party:
# #     def __init__(self,Guest_Name): #constuctor
# #         self.Guest_Name = Guest_Name
# #     @staticmethod
# #     def greet(name):
# #         print(f"Welcome to the party {name} !")  

# # guest1 = Party("Jyoti")
# # print(guest1.Guest_Name)
# # guest1.greet(guest1.Guest_Name)

# #IMPORTANT CONCEPT OF OPPS 

# #1. Abstraction
# #Hiding the implementation details of a class and only showning the essential features to the user

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clch = False
#     def start(self):
#         self.clch = True
#         self.acc = True
#         self.brk = False
#         print("Car started bhrrumm bhruummm")
#     def stop(self):
#         self.clch = True
#         self.brk = True
#         self.acc = False
#         print("Car breaking system activated ciinnuunn")
        
# car1 = car()
# car1.start() #only print Car started bhrrumm bhruummm NO EXTRA INFORMATION OF TURE AND FALSE

# #ENCAPSULATION
# #Wrapping data and function into a single unit (object)

# # del keyword -- used to delete object property or object itself
# del car1 #from here onward no car1 object will be there so if i try to print anything related to car1 it will throw an error

# #PRIVATE ATTRIBUTE & METHOD
# #-->>  Private attributes and methods are meant to be used only within the class and are not accessible from outside the class
# # for declaring it private we use __

# class person:
#     __name ="anonymous"

# p1 = person()
# print(p1.__name)

#***INHERITANCE***
# When one class (child/derived) posses the properties of another class(parent/base)
print

