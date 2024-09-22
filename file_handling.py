# file=open('armstrong.py','r')
# for each in file:
#     print(each)

# f=open("armstrong.py","r")
# print(f.readline())
# print(f.readline())
# f.close()

# file=open("armstrong.py","r")
# print(file.read())

# with open("armstrong.py")as file:
#     data=file.read()
# print(data)

# file=open("armstrong.py","r")
# print(file.read(5))   


# with open("armstrong.py","r")as file:
#     data=file.readlines()
# for line in data:
#     word=line.split()
#     print(word)


# file=open('task_management.py','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()

# with open("task_management.py","w")as f:
#     f.write("Hello World")

file=open("task_management.py",'a')
file.write("\nThis will add this line")
file.close()