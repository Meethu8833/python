l=[]
def registration():
    d={}
    print("\nRegistration:")
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    phone=input("Enter your phone number: ")
    u_name=input("Enter Username: ")
    for i in l:
        if i["Username"]==u_name:
            print("Username already exists!")
            registration()
    pas=input("Enter password: ")
    d["Name"]=name
    d["Age"]=age
    d["Phone number"]=phone
    d["Username"]=u_name
    d["Password"]=pas
    l.append(d)

def login():
    n=input("username: ")
    p=input("password: ")
    val=0
    for i in l:
        if i["Username"]==n and i["Password"]==p:
            val=1
            print("Logged in successfully.....")
    if val==0:
        print("No user found!")

while True:
    print("MAIN MENU:")
    print("1.Registration\n2.Login\n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        registration()
    elif ch==2:
        login()
    elif ch==3:
        print("Exit!!")
        break
    else:
        print("Invalid Choice!")
        