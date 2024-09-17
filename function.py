# def sum(a,b):
#     return a+b
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print("sum is :",sum(a,b))

# def square(n):
#     return n**2
# n=int(input("Enter a number: "))
# print("The square of the given number is: ",square(n))

# def length(s):
#     return len(s)
# a=input("Enter a string: ")
# b=input("Enter another string: ")
# print(length(a))
# print(length(b))


# _______________function arguments_________________
# 1.default arguments

# def fun(n1,n2=20):
#     print("Number 1 is:",n1)
#     print("Number 2 is:",n2)
# n=int(input("Enter a number: "))
# print("Passing only one argument")
# fun(n)

# 2.keyword arguments

# def fun(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("Without using keyword")
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# fun(n2=a,n1=b)


# ____________Anonymous Function________________
# a=lambda c,d:c+d
# n1=int(input("Number 1: "))
# n2=int(input("Number 2: "))
# print("Value of the function is: ",a(n1,n2))


# ____________Nested function_____________
# def word():
#     s=input("Enter a string: ")
#     x=5
#     def number():
#         print(s)
#         print(x)
#     number()
# word()


# _____________Recursive function_____________
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
n=int(input("Enter a number: "))
print("Factorial of",n,"is:",factorial(n))
