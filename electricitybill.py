n=int(input("Enter the number of units consumed: "))
# print(n)
if(n<=100 and n>0):
    print("The total cost is: ",n*5)   
elif(n<=200 and n>100):
    n=n-100
    a=100*5
    b=n*10
    print("The total cost is: ",a+b)
elif(n>200):
    n=n-200
    c=100*10
    a=100*5
    b=n*15
    print("The total cost is: ",a+b+c)
else:
    print("invalid number of units")

