d={}
even=""
odd=""
for i in range(1,11):
    if i%2==0:
        a=str(i)
        even=even+" " +a
    else:
        b=str(i)
        odd=odd+" "+b

d[odd]=even
print(d)
