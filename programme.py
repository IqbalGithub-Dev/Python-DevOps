# def Len_Play():
#     User_choice = input("please enter 1 for word and 2 for list")
#     User_input = input("please enter here ")
#     if User_choice == "1":
#         print("The lenght is",len(User_input))
#     elif User_choice == "2":
#         New_Data = User_input.split(",")
#         print("The length is",len(New_Data))

# Len_Play()

# cities = ("Bhubaneswar","Puri","Cuttack","Ganjam","Balasore")
# person = ("cigii","cuffffiii","juciyyy","dugggiii","guffi","alu","PG")

# def length_List(list):
#     print("the length is ",len(list))


# def print_List(list):
#     for i in list :
#         print(i,end=" ")

# print_List(cities)

#FIND THE FACTORIAL OF N
# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#     print(result)
    
# fact(5)

#function to check even or odd

# def chk():
#     n = int(input("Please enter a number: "))
#     if n== 0 :
#         print("Please be serious bro")
#     elif n%2 ==0:
#         print("The number you have entered is even")
#     else:
#         print("The number you have entered is ODD")

# chk()

# with open("practice2.txt","r") as f :
#     data = f.read()
#     count = 0
#     New_data = [int(num) for num in data.split(",")]
#     for i in New_data :
#         if i%2 == 0:
#             print("Number is even that is : ",i)
#             count += 1
#         else:
#             print("Number is odd  that is : ",i)
#     print("Total even number in this file is : ",count)

with open("opps.py","w") as f :
    f.write("#Welcome to this code")