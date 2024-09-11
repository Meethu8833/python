d={}
id=1
while True:
    print("MENU: ")
    print("1.Registration\n2.Display\n3.Exit")
    n=int(input("Enter your choice: "))  
    if(n==1):
        d1={"name":"","age":"","mark":""}
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        mark=int(input("Enter your mark: "))
        d1["name"]=name
        d1["age"]=age
        d1["mark"]=mark
        d[id]=d1
        id+=1
    elif(n==2):
        na=input("Enter the name: ")
        val=0
        for i in d:  
            if(d[i]["name"]==na):
                # print("inside")
                print(d[i])
                val=1
        if(val==0):
            print("Not found")
    elif(n==3):
        print("Exit!!!")
        break
    else:
        print("Invalid Choice!")



