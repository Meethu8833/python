data=(0,1,2,3,2,3,1,3,2)
print(data)

my_tuple=()
print(type(my_tuple))
print(my_tuple)

my_tuple=("mouse",[8,4,6],(1,2,3))
print(my_tuple)

print("indexing:")
letters=("p","r","o","g","r","a","m","i","z")
print(letters[0])
print(letters[5])


print("negative indexing")
print(letters[-1])
print(letters[-3])

print("slicing")
print(letters[1:4])
print(letters[:-7])
print(letters[7:])
print(letters[:])

print("Repetition tuple")
my_tuple=my_tuple*3
print("New tuple is: ",my_tuple)

print("Tuple methods")
print(letters.count('p'))
print(letters.index('g'))

print("tuple iteration")
for i in letters:
    print(i)

print("Exists of not")
print('c' in letters)
print('p' in letters)
