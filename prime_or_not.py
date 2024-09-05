no=int(input("Enter the number: "))
val=0
for i in range(2,no):
    # print(i)
    if(no%i==0):
        val=1
if(val==0 and no!=1):
    print(no,"is a prime number")
else:
    print(no,"is not a prime number")

