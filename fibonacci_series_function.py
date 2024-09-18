# def fibonacci(f1,f2,n):
#     if n==1:
#         print("0")
#     else:
#         print(f1)
#         print(f2)
#         for i in range(n):
#             f=f1+f2
#             print(f," ")
#             f1=f2
#             f2=f
# n=int(input("Enter the limit: "))
# f1=0
# f2=1
# fibonacci(f1,f2,n-2)



l=[]
def fibonacci(f1,f2,n):
    l.append(0)
    l.append(1)
    for i in range(100):
        f=f1+f2
        l.append(f)
        f1=f2
        f2=f 
    for i in l:
        if i<=n:
            print(i," ")
    
n=int(input("Enter the number: "))
f1=0
f2=1
if n==0:
    print(f1)
elif n==1:
    print(f1)
    print(f2)
    print(f1+f2)
else:
    fibonacci(f1,f2,n)