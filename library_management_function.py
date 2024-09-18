b_l=[]
id=1

def add_book():
        l=[]
        global id
        l.append(id)
        title=input("Enter the book title: ")
        for i in b_l:
            if i[1]==title:
                print("Book already exists!")
                print("Try another title")
                add_book()
        l.append(title)
        author=input("Enter the author name: ")
        l.append(author)
        quantity=int(input("Enter the quantity: "))
        l.append(quantity)
        b_l.append(l)
        id=id+1

def update_book():
    u_id=int(input("Enter the book id to update: "))
    val=0
    for i in b_l:
        if i[0]==u_id:
            val=1
            print("Book id:",i[0])
            print("Book title:",i[1])
            print("Author:",i[2])
            print("Quantity:",i[3])
            while True:
                print("\nWhat to update")
                print("1.Title\n2.Author\n3.Quantity\n4.Exit")
                ch2=int(input("Enter your choice: "))
                if ch2==1:
                    n_title=input("Enter new title: ")
                    for j in b_l:
                        if j[1]==n_title:
                            print("Book title already exists!")
                            update_book()
                    i[1]=n_title
                elif ch2==2:
                    n_author=input("Enter author name to update: ")
                    i[2]=n_author
                elif ch2==3:
                    n_quantity=int(input("Enter quantity to update: "))
                    i[3]=n_quantity
                elif ch2==4:
                    print("Exit!!")
                    break
                else:
                    print("Invalid choice!!")
    if val==0:
        print("Id not found!")
def delete_book():
    d_id=int(input("Enter the id to delete: "))
    val=0
    for i in b_l:
        if i[0]==d_id:
            val=1
            b_l.remove(i)
            print("Removed Successfully...")
    if val==0:
        print("Id not found!")
def display_books():
    print("\n\nAll books in Library:")
    for i in b_l:
        print("\nId:",i[0])
        print("Book title:",i[1])
        print("Author:",i[2])
        print("Quantity:",i[3])


def admin():
    username=input("Enter username: ")
    password=input("Enter the password: ")
    if admin_details[0]==username and admin_details[1]==password:
        while True:
            print("\nADMIN MENU:")
            print("1.Add Book\n2.Update Book\n3.Delete Book\n4.Display All Books\n5.Exit")
            ch1=int(input("Enter your choice: "))
            if ch1==1:
                add_book()
            elif ch1==2:
                update_book()
            elif ch1==3:
                delete_book()
            elif ch1==4:
                display_books()
            elif ch1==5:
                break
            else:
                print("Invalid choice!!")
    else:
        print("Username or Password Invalid!")

def search_book():
    s_book=input("Enter the book title to search: ")
    val=0
    for i in b_l:
        if i[1]==s_book:
            val=1
            print("Id:",i[0])
            print("Book Title:",i[1])
            print("Author:",i[2])
            print("Quantity:",i[3])
    if val==0:
        print("No book found!")
user_details=[]
def registration():
    u=[]
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    address=input("Enter your address: ")
    val=1
    while val==1:
        val=0
        number=input("Enter Phone number: ")
        for i in user_details:
            if i[5]==number:
                val=1
                print("Phone number already exists!\nTry another")
    val=1
    while val==1:
        val=0
        u_name=input("Enter username: ")
        for i in user_details:
            if i[0]==u_name:
                val=1
                print("Username already exist!\nTry another")
    pas=input("Enter password: ")
    u.append(u_name)
    u.append(pas)
    u.append(name)
    u.append(age)
    u.append(address)
    u.append(number)
    user_details.append(u)
    print("Successfully Registered...")


def login():
        l_name=input("Enter your Username: ")
        l_pas=input("Enter your password: ")
        val=0
        for i in user_details:
            if l_name==i[0] and l_pas==i[1]:
                val=1
                while True:
                    print("1.Display All Books\n2.Search Book\n3.Exit")
                    ch1=int(input("Enter your choice: "))
                    if ch1==1:
                        display_books()
                    elif ch1==2:
                        search_book()
                    elif ch1==3:
                        print("Exit!")
                        break
                    else:
                        print("Invalid choice!!")
        if val==0:
            print("Invalid Username or password!")

def user():
    print("\nUSER MENU:")
    while True:
        print("1.Registration\n2.Login\n3.Exit")
        ch1=int(input("Enter your choice: "))
        if ch1==1:
            registration()
        elif ch1==2:
            login()
        elif ch1==3:
            print("Exit!")
            break
        else:
            print("Invalid choice!")

admin_details=["admin","123"]
while True:
    print("MAIN MENU:")
    print("1.Admin\n2.User\n3.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        admin()
    elif ch==2:
        user()
    elif ch==3:
        break
    else:
        print("Invalid choice!")