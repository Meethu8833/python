n=9
for i in range(n):
    for j in range(5):
        if(i==0 or j==0 or i==n-1 or i==4 or (i>4 and j==4)):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
