m_l=[]
val=0
while True:
    print("\n\n1.ADD TASK\n2.VIEW ALL TASKS\n3.UPDATE TASK\n4.MARK TASK AS COMPLETED\n5.DELETE TASK\n6.SEARCH TASK BY NAME\n7.EXIT")
    ch=int(input("Enter the choice: "))
    if ch==1:
        print("\nAdd task:")
        l=[]
        name=input("Enter the name of task: ")
        name=name.upper()
        val=0
        for i in m_l:
            if i[0]==name:
                print(".....Task Already Exists!.....")
                val=1
        if(val==0):       
            des=input("Description: ")
            date=input("Due Date: ")
            lvl=input("Priority Level(High,Medium,Low): ")
            lvl=lvl.lower()
            if lvl=="high" or lvl=="medium" or lvl=="low":
                l.append(name)
                l.append(des)
                l.append(date)
                l.append(lvl)
                l.append("Not Completed")
                m_l.append(l)
            else:
                print("Invalid level!")
            
    elif ch==2:
        print("\nAll Tasks:")
        num=1
        for i in m_l:
            print(num,". ",i[0])
            print("Description: ",i[1])
            print("Due Date: ",i[2])
            print("Priority: ",i[3])
            print("Completion Status:",i[4],"\n")
            num+=1
    elif ch==3:
        print("\nUpdate Task:")
        ta=input("Enter the name of the task to update: ")
        val=0
        for i in m_l:
            if i[0]==ta.upper():
                val=1
                print("\nTask Details:")
                print("Task name:",i[0])
                print("Description:",i[1])
                print("Due Date:",i[2])
                print("Priority:",i[3])
                print("Completion Status:",i[4],"\n")
                print("What to update: ")
                while True:
                    print("1.Task name\n2.Description\n3.Due date\n4.Priority\n5.Exit")
                    ch1=int(input("Enter your choice to update details: "))
                    if ch1==1:
                        u_name=input("Enter name to update: ")
                        u_name=u_name.upper()
                        val1=0
                        for j in m_l:
                            if j[0]==u_name:
                                print("Task already exists!")
                                val1=1
                        if val1==0:
                            i[0]=u_name
                            print("Successfully Updated....")
                    elif ch1==2:
                        u_des=input("Enter description to update: ")
                        i[1]=u_des
                        print("Successfully Updated....")
                    elif ch1==3:
                        u_date=input("Enter date to update: ")
                        i[2]=u_date
                        print("Successfully Updated....")
                    elif ch1==4:
                        u_prio=input("Enter priority to update: ")
                        u_prio=u_prio.lower()
                        if u_prio=="high" or u_prio=="medium" or u_prio=="low":
                            i[3]=u_prio
                            print("Successfully Updated....")
                        else:
                            print("Invalid level!")
                    elif ch1==5:
                        print("Exit from update section")
                        break
                    else:
                        print("Invalid choice!!")
        
        if val==0:
            print("Task name not found!")
        
    elif ch==4:
        print("\nMark Task as Completed:")
        m_name=input("Enter the task name: ")
        m_name=m_name.upper() 
        val=0
        for i in m_l:
            if i[0]==m_name:
                val=1
                i[4]="Completed"
        if val==0:
            print("Task not found")
        else:
            print("Task updated to completed...")
    elif ch==5:
        print("\nDelete Task:")
        d_name=input("Enter the name of task to delete: ")
        d_name=d_name.upper()
        val=0
        for i in m_l:
            if i[0]==d_name:
                val=1
                m_l.remove(i)
        if val==0:
            print("Task not found!")
        else:
            print("Task Deleted Successfully..")
    elif ch==6:
        print("\nSearch Task:")
        s_name=input("Enter the task name: ")
        s_name=s_name.upper()
        val=0
        for i in m_l:
            if i[0]==s_name:
                val=1
                print("Task name:",i[0])
                print("Description: ",i[1])
                print("Due Date: ",i[2])
                print("Priority: ",i[3])
                print("Completion Status:",i[4],"\n")
        if val==0:
            print("Task not found!")
    elif ch==7:
        # print(d)
        break
    else:
        print("Invalid Choice!!!!")

