def armstrong(n):
    if n==0:
        return 0
    else:
        rem=n%10
        a=rem**l
        n=int(n/10)
        return (a+armstrong(n))
       
n=int(input("Enter a number: "))
s=str(n)
l=len(s)
val=armstrong(n)
if val==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")
