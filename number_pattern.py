n=4
a=1

for j in range(n+1):
    if(j==n-1):
        print(a)
        for k in range(n-1):
            print(a)
            a=a+1
    elif(j<n):
        print(a,end=" ")
        a=a+1
    

