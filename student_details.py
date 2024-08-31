list_of_students=[]
n=int(input("Enter the number of students"))
id=0

for i in range(n):
    d={"ID":"","Name":"","Age":"","Marks":""}
    name=input("Enter the name of student: ")
    age=input("Enter the age: ")
    m1=int(input("Mark of subject 1: "))
    m2=int(input("Mark of subject 2: "))
    m3=int(input("Mark of subject 3: "))
    id=id+1
    d["ID"]=id
    d["Name"]=name
    d["Age"]=age
    d["Marks"]=[m1,m2,m3]
    list_of_students.append(d)
   
print(list_of_students)
    