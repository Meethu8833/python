n=int(input("Enter the number of elements:"))
l=[]
print("Enter the elements:")
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    for j in range(i,n):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("The second largest number is",l[n-2])

