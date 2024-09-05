n=int(input("Enter the number of students: "))
dic1={}
for i in range(n):
    dic2={'name':'','age':'','city':''}
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    city=input("Enter you city: ")
    dic2['name']=name
    dic2['age']=age
    dic2['city']=city
    dic1[i+1]=dic2
print(dic1)
    
for i in dic1:
    print(dic1[i])
print("...",dic1)