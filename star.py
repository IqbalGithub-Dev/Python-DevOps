# for row in range(6):

#     for col in range(6):

#         if row == 0 or row == 5 or col == 0 or col == 5:
#             print("*", end="")

#         else:
#             print(" ", end="")

#     print()

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f :
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("Not found")

def chk_for_line():
    word = "Python"
    data = True
    line_no = 1
    with open ("practice.txt","r") as f :
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                #return
            line_no += 1
            
    return -1
chk_for_line()