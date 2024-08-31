l=[1,2,3,4,5,6,7,8,9,10,11,13]
c1=0
c2=0
for i in l:
    if(i%2==0):
        c1=c1+1
    else:
        c2=c2+1
print("The number of even numbers is: ",c1)
print("The number of odd numbers is: ",c2)
