n=10
for i in range(n):
    for j in range(n):
        if(i<int(n/2)):
            if(j<i+1 or j>n-i-2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if(j<n-i-1 or j>i):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()