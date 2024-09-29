class Student:
    def display_details(self):
        length=len(lis)
        print("_________Students Details________")
        for i in range(length):
            print("Name:",lis[i][0])
            print("Age:",lis[i][1])
            print("Grade:",lis[i][2],"\n")

lis=[]
class Menu:
    def add_student(self):
        l=[]
        n=input("Enter student's name: ")
        a=int(input("Enter the age: "))
        g=input("Enter the grade: ")
        l=[n,a,g]
        lis.append(l)
    def run(self):
        while True:
            print("1.Add Student\n2.Display Student\n3.Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                self.add_student()
            elif n==2:
                d=Student()
                d.display_details()
            elif n==3:
                break
            else:
                print("Invalid choice!")
m=Menu()
m.run()










