m_l=[]
while True:
    print("1.Registration\n2.Display\n3.Exit ")
    n=int(input("Enter your choice: "))
    if(n==1):
        lis=[]
        print("REGISTRATION: ")
        name=input("Enter your name: ")
        lis.append(name)
        age=int(input("Enter your age: "))
        lis.append(age)
        mark=int(input("Enter your mark: "))
        lis.append(mark)
        m_l.append(lis)
    elif(n==2):
        print("Display: ")
        val=0
        # print(m_l)
        na=input("Enter your name: ")
        for i in m_l:
            if i[0]==na:
                print("Name:",i[0])
                print("Age:",i[1])
                print("Mark: ",i[2])
                val=1
        if(val==0):
            print("Not Found!")
    elif(n==3):
        print("Exit!")
        break
    else:
        print("Invalid Choice!")




