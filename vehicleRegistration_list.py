m_l=[]
while True:
    print("1.REGISTRATION\n2.DISPLAY\n3.EXIT")
    ch=int(input("Enter your choice: "))
    if ch==1:
        l=[]
        print("\nRegistration:")
        v_name=input("Enter name of vehicle: ")
        m_name=input("Enter Model name of vehicle: ")
        tyres=int(input("Enter number of tyres(2,3,4): "))
        o_name=input("Enter owner's name: ")
        l.append(tyres)
        l.append(v_name)
        l.append(m_name)
        l.append(o_name)
        m_l.append(l)
    elif ch==2:
        while True:
            print("\nDisplay: ")
            print(m_l)
            print("1. 2 Tyres\n2. 3 Tyres\n3. 4 Tyres \n4. Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                val=0
                for i in m_l:
                    if i[0]==2:
                        print("Model of vehicle : ",i[1])
                        print("Vehicle name : ",i[2])
                        print("Owner name : ",i[3])
                        print("Number of tyres: ",i[0],"\n")
                        val=1
                if val==0:
                    print("No vehicles found!")
            elif n==2:
                val=0
                for i in m_l:
                    if i[0]==3:
                        print("Model of vehicle : ",i[1])
                        print("Vehicle name : ",i[2])
                        print("Owner name : ",i[3])
                        print("Number of tyres: ",i[0],"\n")
                        val=1
                if val==0:
                    print("No vehicles found!")
            elif n==3:
                val=0
                for i in m_l:
                    if i[0]==4:
                        print("Model of vehicle : ",i[1])
                        print("Vehicle name : ",i[2])
                        print("Owner name : ",i[3])
                        print("Number of tyres: ",i[0],"\n")
                        val=1
                if val==0:
                    print("No vehicles found!")
            elif n==4:
                break
            else:
                print("Invalid number of tyres!")
    elif ch==3:
        print("Exit!")
        break
    else:
        print("Invalid Choice!")


