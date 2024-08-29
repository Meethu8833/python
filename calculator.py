c=int(input("\nMenu 1:Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit\n"))


if(c==1):
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a,"+",b,"=",a+b)
elif(c==2):
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a,"-",b,"=",a-b)
elif(c==3):
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a,"*",b,"=",a*b)
elif(c==4):
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a,"/",b,"=",a/b)
elif(c==5):
    exit()
else:
    print("Invalid choice")


