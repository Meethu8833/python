# d={}
# while True:
#     print("1.ADD TASK\n2.VIEW ALL TASKS\n3.UPDATE TASK\n4.MARK TASK AS COMPLETED\n5.DELETE TASK\n6.SEARCH TASK BY NAME\n7.EXIT")
#     ch=int(input("Enter the choice: "))
#     if ch==1:
#         print("\nAdd Task:")
#         lis=[]
#         val=0
#         name=input("Task Name: ")
#         name=name.upper()
#         for i in d:
#             if i==name:
#                 print(".....Task Already Exists!.....")
#                 val=1
#         if(val==0):       
#             des=input("Description: ")
#             date=input("Due Date: ")
#             lvl=input("Priority Level(High,Medium,Low): ")
#             lis.append(des)
#             lis.append(date)
#             lis.append(lvl)
#             lis.append("Not Completed")
#             d[name.upper()]=lis
#     elif ch==2:
#         print("\nAll Tasks:")
#         num=1
#         for i in d:
#             print(num,". ",i)
#             print("Description: ",d[i][0])
#             print("Due Date: ",d[i][1])
#             print("Priority: ",d[i][2])
#             print("Completion Status:",d[i][3],"\n")
#             num+=1
#     elif ch==3:
#         print("\nUpdate Task:")
#         ta=input("Enter the name of the task to update: ")
#         val=0
#         for i in d:
#             if i==ta.upper():
#                 val=1
#                 print("Task name:",i)
#                 print("Description: ",d[i][0])
#                 print("Due Date: ",d[i][1])
#                 print("Priority: ",d[i][2])
#                 print("Completion Status:",d[i][3],"\n")
#                 # print("What to update: ")
#                 while True:
#                     print("1.Task name\n2.Description\n3.Due date\n4.Priority\n5.Exit")
#                     ch1=int(input("Enter your choice to update details: "))
#                     if ch1==1:
#                         u_name=input("Enter name to update: ")
#                         u_name=u_name.upper()
#                         val=0
#                         for j in d:
#                             if j==u_name:
#                                 print("Task already exists!")
#                                 val=1
#                         if val==0:
#                             i=u_name
#                     elif ch1==2:
#                         u_des=input("Enter description to update: ")
#                         d[i][0]==u_des
#                     elif ch1==3:
#                         u_date=input("Enter date to update: ")
#                         d[i][1]==u_date
#                     elif ch1==4:
#                         u_prio=input("Enter priority to update: ")
#                         d[i][2]=u_prio
#                     elif ch1==5:
#                         print("Exit from update section")
#                         break
#                     else:
#                         print("Invalid choice!!")
        
#         if val==0:
#             print("Task name not found!")
#         else:
#             print("Successfully Updated....")
        
#     elif ch==4:
#         print("\nMark Task as Completed:")
#         m_name=input("Enter the task name: ")
#         m_name=m_name.upper() 
#         val=0
#         for i in d:
#             if i==m_name:
#                 val=1
#                 d[i][3]="Completed"
#         else:
#             print("Task updated to completed...")
#         if val==0:
#             print("Task not found")
#     elif ch==5:
#         print("\nDelete Task:")
#         d_name=input("Enter the name of task to delete: ")
#         d_name=d_name.upper()
#         val=0
#         for i in d:
#             if i==d_name:
#                 val=1
#                 del d[i]
#         else:
#             print("Task Deleted Successfully..")
#         if val==0:
#             print("Task not found!")
#     elif ch==6:
#         print("\nSearch Task:")
#         s_name=input("Enter the task name: ")
#         val=0
#         for i in d:
#             if i==s_name:
#                 val=1
#                 print("Task name:",i)
#                 print("Description: ",d[i][0])
#                 print("Due Date: ",d[i][1])
#                 print("Priority: ",d[i][2])
#                 print("Completion Status:",d[i][3],"\n")
#         if val==0:
#             print("Task not found!")
#     elif ch==7:
#         # print(d)
#         break
#     else:
#         print("Invalid Choice!!!!")

tasks = []
while True:
    print("Main Menu:")
    print("1.Add Task")
    print("2.View All Tasks")
    print("3.Update Task")
    print("4.Mark Task as Completed")
    print("5.Delete Task")
    print("6.Search Task by Name")
    print("7.Exit")
    choice = input("Enter your choice: ")

    if choice =='1':
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_due_date = input("Enter task due date: ")
        task_priority = input("Enter task priority: ")
        task = {'name': task_name,'description': task_description,'due_date': task_due_date,'priority': task_priority,'completed': False}
        tasks.append(task)
        print("Task added ")
    elif choice == '2':
        for task in tasks:
            print("Name:", task['name'])
            print("Description:", task['description'])
            print("Due Date:", task['due_date'])
            print("Priority:", task['priority'])
            print("Completed:", task['completed'])
    elif choice == '3':
        search_name = input("Enter the task  to update: ")
        task_found = False
        for task in tasks:
            if task['name']== search_name:
                task_found = True
                task['name'] = input("Enter new task name: ")
                task['description'] = input("Enter new task description: ")
                task['due_date'] = input("Enter new task due date: ")
                task['priority'] = input("Enter new task priority")
                print("Task updated ")
                break
        if not task_found:
            print("Task not found")
    elif choice =='4':
        search_name = input("Enter the task name to mark as completed: ")
        task_found = False
        for task in tasks:
            if task['name']== search_name:
                task_found =True
                print("Task marked as completed.")
        if not task_found:
            print("Task not found.")
    elif choice == '5':
        search_name = input("Enter the name of the task  to delete: ")
        task_found = False
        for task in tasks:
            if task['name'] ==search_name:
                task_found = True
                tasks.remove(task)
                print("Task deleted ")
                break
        if not task_found:
            print("Task not found")
    elif choice =='6':
        search_name = input("Enter the task name to search: ")
        task_found = False
        for task in tasks:
            if task['name'] == search_name:
                task_found = True
                print("Name:", task['name'])
                print("Description:", task['description'])
                print("Due Date:", task['due_date'])
                print("Priority:", task['priority'])
                print("Completed:",task['completed'])
                break
        if not task_found:
            print("Task not found.")
    else:
        if choice=='7':
            print("Exiting the program.")
            break
        else:
            print("invalid choice :")