a=input("Enter a string to check whether it is palindrome: ")
b=a[::-1]
if(a==b):
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")