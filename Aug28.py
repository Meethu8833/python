a=('a','b','c','d')
print(type(a))
print(a)
a=list(a)
print(type(a))
a[1]='z'
print("changed list",a)
a=tuple(a)
print(type(a))


set1={1,2,3,4}
set2={3,4,5,6}
print("set 1 ",set1)
print("set 2 ",set2)
print("Union of two sets:",set1|set2)
print("Intersection of two sets: ",set1&set2)


details={"name":"John","age":25,"city":"New York"}
print(details)
details["age"]=30
print("Updated dictionary: ",details)
details["job"]="Engineer"
print("dictionary after key added: ",details)


list1=[1,2,3,4,5]
print(list1)
list1=tuple(list1)
print("tuple: ",list1)


d1={'x':10,'y':20}
d2={'z':30}
print("Merged dictionary: ",d1|d2)