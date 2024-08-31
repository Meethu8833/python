s=input("Enter the string: ")
c=input("Enter the character: ")
l=len(s)
count=0
for i in range(l):
    if(c==s[i]):
        count=count+1
print("The number of time the character occured is:",count)
