l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    a=int(input("Enter the element: "))
    l.append(a)

l1=[]
for i in range(n):
    val=0
    for j in range(n):
        if(l[i]==l[j] and i!=j):
            # print(val)
            val=1
    if(val==0):
        # print(l[i])
        l1.append(l[i])

length=len(l1)
if(length==0):
    print("Null")

else:
    min=l1[0]
    for i in range(length):
        if(min<l1[i]):
            min=l1[i]
    print("The largest is:",min) 
