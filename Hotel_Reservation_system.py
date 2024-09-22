admin_details=["mee","111"]
receptionist_details=["res","2"]
rooms=[]
guests=[]
count=101
def add_room():
    l=[]
    global count
    no=count
    type=input("Enter the type of room(single,double,suite): ")
    if type not in ["single","double","suite"]:
        print("Invalid type!")
        add_room()
    price=int(input("Enter the price per night: "))
    status="available"
    l.append(no)
    l.append(type)
    l.append(price)
    l.append(status)
    rooms.append(l)
    count+=1

def update_room():
    no=int(input("Enter the room number to update: "))
    for i in rooms:
        if i[0]==no:
            print("Room Details:::")
            print("Room No: ",i[0])
            print("Type: ",i[1])
            print("Price: ",i[2])
            print("Availablity Status: ",i[3],"\n")
            while True:
                print("What to update:")
                print("1.Price\n2.Availability Status\n3.Exit")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    price=input("Enter new price: ")
                    i[2]=price
                    print("Updated Successfully...")
                elif ch1==2:
                    status=input("Enter the current status: ")
                    i[3]=status
                    print("Updated Successfully...")
                elif ch1==3:
                    break
                else:
                    print("Invalid choice!!!")
def remove_room():
    no=int(input("Enter the room number to remove: "))
    val=0
    for i in rooms:
        if i[0]==no:
            val=1
            rooms.remove(i)
            print("Removed Successfully..")
    if val==0:
        print("Room Not Found!!")
def view_reservations():
    for i in reservation:
        print("Room No:",i[2])
        print("Reservation ID:",i[0])
        print("Guest ID:",i[1])
        print("Check-in Date:",i[3])
        print("Check-out Date:",i[4],"\n")
def generate_reports():
    count=0
    c=0
    for i in rooms:
        if i[3]=="occupied":
            count+=1
        elif i[3]=="available":
            c+=1
    print("Occupancy Rate:",count)
    print("Available Rooms:",c)
def admin():
    name=input("Enter your username: ")
    pas=input("Enter your password: ")
    if admin_details[0]==name and admin_details[1]==pas:
        while True:
            print("\nADMIN MENU:")
            print("1.Add Room\n2.Update Room Details\n3.Remove Room\n4.View All Reservations\n5.Generate Reports\n6.Exit")
            ch1=int(input("Enter your choice: "))
            if ch1==1:
                add_room()
            elif ch1==2:
                update_room()
            elif ch1==3:
                remove_room()
            elif ch1==4:
                view_reservations()
            elif ch1==5:
                generate_reports()
            elif ch1==6:
                print("Exit From Admin menu!")
                break
            else:
                print("Invalid Choice!!")
    else:
        print("Invalid username or password!\nTry again")
        admin()

reservation=[]
r_id=1
check=[]
def check_in():
    l=[]
    id=int(input("Enter the guest ID: "))
    val1=0
    for i in guests:
        if i[0]==id:
            val1=1
    if val1==0:
        print("Invalid guest id!")
        check_in()
    no=int(input("Enter the room Number: "))
    val=0
    for i in rooms:
        if i[0]==id:
            val=1
            i[3]="occupied"
    if val==0:
        print("Invalid Room number!")
        check_in()
    date=input("Enter the check-in date: ")
    l.append(id)
    l.append(no)
    l.append(date)
    check.append(l)
    print("Check-in Successfull..")
       
def check_out():
    id=int(input("Enter the guest ID: "))
    no=int(input("Enter the room no: "))
    val=0
    for i in check:
        if i[0]==id and i[1]==no:
            val=1
            for j in rooms:
                if j[0]==i[1]:
                    j[3]=="available"
            check.remove(i)
    if val==0:
        print("Invalid guest id or room number!")
        check_out()

def make_reservation():
    l=[]
    global r_id
    print("Available Rooms:")
    val=0
    for i in rooms:
        if i[3]=="available":
            val=1
            print(i[0])
    if val==0:
        print("No Rooms Available!")
    else:
        g_details=input("Enter the guest id: ")
        r_no=int(input("Enter the room no: "))
        for j in rooms:
            if j[0]==r_no:
                j[3]="reserved"
        c_in=input("Enter check-in date: ")
        c_out=input("Enter the check-out date ")
        l.append(r_id)
        l.append(g_details)
        l.append(r_no)
        l.append(c_in)
        l.append(c_out)
        reservation.append(l)
        r_id+=1
        print("Room Reserved....")
def cancel_reservation():
    id=int(input("Enter the reservation id: "))
    guest_id=int(input("Enter the guest id: "))
    val=0
    for i in reservation:
        if i[0]==id and i[1]==guest_id:
            val=1
            for j in rooms:
                if j[0]==i[2]:
                    j[3]=="available"
                    reservation.remove(i)
    if val==0:
        print("No Reservation found!")
def view_available_rooms():
    print("Available rooms:")
    val=0
    for i in rooms:
        if i[3]=="available":
            val=1
            print("Room No: ",i[0])
            print("Type: ",i[1])
            print("Price: ",i[2])
            print("Availablity Status: ",i[3],"\n")
    if val==0:
        print("No Rooms Available!")
def view_guest_details():
    print("Guest Details:")
    for i in guests:
        print("Guest ID:",i[0])
        print("Name:",i[1])
        print("Phone Number:",i[2])
        print("Address:",i[3],"\n")
        


def receptionist():
    r_name=input("Enter the username: ")
    r_pas=input("Enter the password: ")
    if receptionist_details[0]==r_name and receptionist_details[1]==r_pas:
        while True:
            print("Receptionist Menu:")
            print("1.Check-in Guest\n2.Check-out Guest\n3.Make Reservation\n4.Cancel Reservation\n5.View Available Rooms\n6.View Guest Details\n7.Exit")
            ch1=int(input("Enter your choice: "))
            if ch1==1:
                check_in()
            elif ch1==2:
                check_out()
            elif ch1==3:
                make_reservation()
            elif ch1==4:
                cancel_reservation()
            elif ch1==5:
                view_available_rooms()
            elif ch1==6:
                view_guest_details()
            elif ch1==7:
                 print("Exit!!")
                 break
            else:
                print("Invalid Choice!!")
    else:
        print("Invalid Username or password!\nTry again")
        receptionist()



g_id=1
def register():
    l=[]
    global g_id
    id=g_id
    name=input("Enter your name: ")
    contacts=input("Enter your phone number: ")
    address=input("Enter your address: ")
    u_name=input("Enter username: ")
    for i in guests:
        if i[4]==u_name:
            print("Username already exists!")
            register()
    pas=input("Enter password: ")
    l.append(id)
    l.append(name)
    l.append(contacts)
    l.append(address)
    l.append(u_name)
    l.append(pas)
    guests.append(l)
    g_id+=1



def view_reservation_status(i):
    val=0
    for j in reservation:
        if i[1]==j[0]:
            val=1
            print("Current Reservation Status: Reserved")
            print("Check-in Date:",j[3])
            print("Check-out Date:",j[4])
    if val==0:
        print("Current Reservation Status:Not Reserved")
    
def update_personal_info(i):
    contact=input("Enter the phone number to update: ")
    address=input("Enter the address to update: ")
    i[2]=contact
    i[3]=address
    print("Successfully Updated...")

def login():
    print("Guest Login:")
    l_name=input("Enter username: ")
    l_pas=input("Enter your password: ")
    val=0
    for i in guests:
        if i[4]==l_name and i[5]==l_pas:
            val=1
            while True:
                print("Guest Menu:")
                print("1.View Available Rooms\n2.Make a Reservation\n3.View Reservation Status\n4.Update Personal Information\n5.Cancel Reservation\n6.Exit")
                ch1=int(input("Enter your choice: "))
                if ch1==1:
                    view_available_rooms()
                elif ch1==2:
                    make_reservation()
                elif ch1==3:
                    view_reservation_status(i)
                elif ch1==4:
                    update_personal_info(i)
                elif ch1==5:
                    cancel_reservation()
                elif ch1==6:
                    print("Exit!!")
                    break
                else:
                    print("Inavalid choice!!")
    if val==0:
        print("Invalid username or password!\nTry agian")
        login()

def guest():
    print("\nGuest Section:")
    while True:
        print("1.Register\n2.Login\n3.Exit")
        ch1=int(input("Enter your choice: "))
        if ch1==1:
            register()
        elif ch1==2:
            login()
        elif ch1==3:
            print("Exit!!")
            break
        else:
            print("Invalid choice!")


while True:
    print("MAIN MENU:\n")
    print("1.Admin\n2.Receptionist\n3.Guest\n4.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        admin()
    elif ch==2:
        receptionist()
    elif ch==3:
        guest()
    elif ch==4:
        print("Exit!")
        break
    else:
        print("Invalid Choice!")