n=4
ind=0
l=[]
for i in range(n):
    for j in range(n-i):
        print("  ",end="")
    for j in range(i+1):
        if(j==0 or j==i):
            l.append(1)
            print(l[ind],end="   ")
        else:
            l.append(l[ind-i-1]+l[ind-i])
            print(l[ind],end="   ")
        ind=ind+1
    print()
    
