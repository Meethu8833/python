n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
l=[]
d={}
for i in range(n):
    a=int(input())
    l.append(a)

k=set(l)
keys=tuple(k)
length=len(k)
for i in range(length):
    count=0
    for j in range(n):
        if(keys[i]==l[j]):
            count=count+1
    d[keys[i]]=count
print(d)