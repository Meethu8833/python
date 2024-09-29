def addition():
    a=int(input("Enter the first no.: "))
    b=int(input("Enter the second no.: "))
    return a+b
def subtraction():
    a=int(input("Enter the first no.: "))
    b=int(input("Enter the second no.: "))
    return a-b
def multiplication():
    a=int(input("Enter the first no.: "))
    b=int(input("Enter the second no.: "))
    return a*b
def division():
    a=int(input("Enter the first no.: "))
    b=int(input("Enter the second no.: "))
    if b==0:
        return "Number can't be divisible by zero"
    else:
        return a/b
class Calculator:
    def menu(self):
        while True:
            print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
            ch=int(input("Enter your choice: "))
            if ch==1:
                print("Sum is: ",addition())
            elif ch==2:
                print("Difference is:",subtraction())
            elif ch==3:
                print("Product is:",multiplication())
            elif ch==4:
                print("Quotient is:",division())
            elif ch==5:
                break
            else:
                print("Invalid choice!")
cal=Calculator()
cal.menu()
            

