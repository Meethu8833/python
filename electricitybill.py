n=int(input("Enter the number of units consumed: "))
# print(n)
if(n<=100 and n>0):
    print("The total cost is: ",n*5)
elif(n<=200 and n>100):
    print("The total cost is: ",n*10)
elif(n>200):
    print("The total cost is: ",n*15)
else:
    print("invalid number of units")