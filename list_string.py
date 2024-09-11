l=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a=input()
    l.append(a)


lis=[i[0] for i in l]
print(lis)
