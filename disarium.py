def disarium():
    l=str(n)
    count=1
    sum=0
    for i in str(n):
         sum=sum+(int(i)**count)
         count+=1
    return sum

n=int(input("Enter the number: "))
x=disarium()
if x==n:
     print(n,"is a disarium number")
else:
     print(n,"is not a disarium number")