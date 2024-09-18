a=input("Enter the number: ")
a1=int(a)
l=len(a)
sum=0

for i in a:
    n=int(i)
    sum=sum+(n**l)

if(a1==sum):
    print(a1,"is an armstrong number")
else:
    print(a1,"is not an armstrong number")