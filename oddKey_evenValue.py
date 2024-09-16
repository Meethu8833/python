d={}
l1=[]
l2=[]

for i in range(1,11):
    if i%2==0:
        l2.append(i)
    else:
        l1.append(i)
t=tuple(l1)
d[t]=l2
print(d)