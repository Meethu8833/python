str=input("Enter the string: ")
s=str.lower()
a={i for i in s if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'}
print(a)