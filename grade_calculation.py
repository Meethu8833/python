mark=int(input("Enter your mark: "))

if(mark>=90 and mark<=100):
    print("A+")
elif(mark>=80 and mark<90):
    print("A")
elif(mark>=70 and mark<80):
    print("B+")
elif(mark>=60 and mark<70):
    print("B")
elif(mark>=50 and mark<60):
    print("C+")
elif(mark>=40 and mark<50):
    print("C")
elif(mark<40 and mark>=0):
    print("Fail")
else:
    print("Invalid mark")