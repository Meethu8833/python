l=[]
lis=[]
def elements(n):
    print("Enter the elements:")
    for i in range(n):
        a=int(input())
        l.append(a)

def unique():
    length=len(l)
    for i in range(length):
        val=0
        for j in range(length):        
            if l[i]==l[j] and i!=j:
                val=1
        if val==0:
            lis.append(l[i])


n=int(input("Enter the size: "))
elements(n)
unique()
print("original list:",l)
print("list after duplicate elements deleted:",lis)