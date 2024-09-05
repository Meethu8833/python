n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    # print(i)
    fact=fact*i
print("The factorial of",n,"is",fact)