from calc_import import*
while True:
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Sum is:",sum(a,b))
    elif ch==2:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Difference is",dif(a,b))
    elif ch==3:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Product is:",pro(a,b))
    elif ch==4:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("Quotient is:",div(a,b))
    elif ch==5:
        break
    else:
        print("Invalid choice!")