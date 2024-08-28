print("Creating a dictionary")
city={"nepal":"kathmandu","italy":"rome"}
print(city)

print("Add elements to dictionary")
print("initial dictionary:",city)
city["japan"]="tokyo"
print("Updated dictionary: ",city)

print("change value of dictionary:")
student_id={111:"eric",112:"kyle",113:"butters"}
print(student_id[111])
print(student_id[113])

print("Removing elements form dictionary")
print("Initial dictionary:",student_id)
del student_id[111]
print("Updated dictionary: ",student_id)

print("Iterating through dictionary")
for i in student_id:
    print(student_id[i])