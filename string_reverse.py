s=input("Enter a string to reverse: ")
l=len(s)
rev=""

for i in range(l):
    # print(s[i])
    rev=s[i]+rev
print(rev)


