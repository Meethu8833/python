# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# newSet = {element*3 for element in myList if element % 2 ==0} 
# print(newSet)


# mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
# newSet = {element ** 2 for element in mySet} 
# print(newSet)


mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} 
print(mySet) 
mySet = {element for element in mySet if element % 2 == 0} 
print(mySet)
