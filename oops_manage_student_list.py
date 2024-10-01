class Student:
    student_list=[]
    r_no=1
    def main_menu(self):
        while True:
            print("\nMenu:")
            print("1.Add a new student\n2.View all students\n3.Update marks of a student\n4.Average marks of students\n5.Exit")
            ch=int(input("Enter your choice: "))
            if ch==1:
                self.add_student()
            elif ch==2:
                self.view_students()
            elif ch==3:
                self.update_marks()
            elif ch==4:
                self.avg_marks()
            elif ch==5:
                exit()
            else:
                print("Invalid choice!")
    def add_student(self):
        l=[]
        name=input("Enter the name of the student: ")
        print("Enter the marks in three subjects:")
        m1=int(input())
        m2=int(input())
        m3=int(input())
        roll_no=self.r_no
        print("Roll Number is:",roll_no)
        l=[name,roll_no,m1,m2,m3]
        self.student_list.append(l)
        self.r_no+=1
        self.main_menu()
    def view_students(self):
        print("All student details:")
        for i in self.student_list:
            print("\nName:",i[0])
            print("Roll Number:",i[1])
            print(f"Marks in three subjects: {i[2]},{i[3]},{i[4]}")
        self.main_menu()
    def update_marks(self):
        st=input("\nEnter the name of the student to update mark: ")
        r=int(input("Enter the roll number:"))
        val=0
        for i in self.student_list:
            if i[0]==st and i[1]==r:
                val=1
                print(f"Marks in three subjects: {i[2]},{i[3]},{i[4]}")
                print("\nEnter the marks to update:")
                i[2]=int(input())
                i[3]=int(input())
                i[4]=int(input())
        if val==0:
            print("Student not exists!")
        else:
            print("Updated Successfully..")
        self.main_menu()
    def avg_marks(self):
        print("Average marks of students:")
        if len(self.student_list)==0:
            print("No students in the list!")
        else:
            for i in self.student_list:
                avg=(i[2]+i[3]+i[4])/3
                print(f"\nName: {i[0]}\nAverage mark: {avg}")
        self.main_menu()
st=Student()
st.main_menu()
