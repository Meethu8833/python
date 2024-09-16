d={}
id=1
while True:
    print("1.Registstation\n2.Login\n3.Exit")
    n=int(input("Enter your choice: "))
    if(n==1):
        f=0
        details={"Username":"","Password":""}
        print("\nREGISTRATION:")
        u_name=input("Username: ")
        for i in d:
            if(d[i]["Username"]==u_name):
                print("Already Exists!")
                f=1
                # u_name=input("Try another username: ")
        if(f==0):
            pas=input("Password: ")
            details["Username"]=u_name
            details["Password"]=pas
            d[id]=details
            id+=1
            print("Registered Successfully..")
    elif(n==2):
        val=0
        print("\nLOGIN:")
        while val==0:
            a=input("Enter your username: ")
            b=input("Enter your password: ")
            for i in d:
                if(d[i]["Username"]==a and d[i]["Password"]==b):
                    print("Successfully Logged In...\n")
                    val=1
            if(val==0):
                print("Try Again")
    elif(n==3):
        print("Exit!!")
        break
    else:
        print("Invalid Choice!")
        