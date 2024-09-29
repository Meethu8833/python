l=[]
n=int(input("Enter the size of the list: "))
print("Enter the elements: ")
for i in range(n):
    a=int(input())
    l.append(a)
original_list=l
l=sorted(l)
min=l[0]
length=len(l)
print("Original list is:",original_list)
print("Sorted list",l)

val=0
for i in original_list:
    if min==i:
        break
    else:
        val=val+1
if min==original_list[0]:
    print("number of times rotated:",length)
else:
    print("number of times rotated:",val)
print("minimum element:",min)