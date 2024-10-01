books=[]
users=[]
class Admin:
    user_name="a"
    password="1"
    id=1
    def admin_login(self):
        u_name=input("Enter username: ")
        pas=input("Enter password: ")
        if u_name==self.user_name and pas==self.password:
            while True:
                print("1.Add Book\n2.Update Book\n3.Delete Book\n4.Display Book\n5.Exit")
                n=int(input("Enter your choice: "))
                if n==1:
                    self.add_book()
                elif n==2:
                    self.update_book()
                elif n==3:
                    self.delete_book()
                elif n==4:
                    self.display_all_books()
                elif n==5:
                    break
                else:
                    print("Invalid choice!")                
    def add_book(self):
        title=input("Enter the book title: ")
        val=0
        for i in books:
            if i[1]==title:
                val=1
                print("Book already exists!")
        if val==0:
            author=input("Enter the author name: ")
            quantity=int(input("Enter the quantity of book: "))
            print("Book ID:",self.id)
            l=[self.id,title,author,quantity]
            books.append(l)
            self.id=self.id+1
        
    def update_book(self):
        b=int(input("Enter the book id to update: "))
        val=0
        for i in books:
            if i[0]==b:
                val=1
                n_t=input("Enter new title to update: ")
                i[1]=n_t
                n_a=input("Enter author name to update: ")
                i[2]=n_a
                n_q=int(input("Enter the quantity to update: "))
                i[3]=n_q
        if val==0:
            print("Book not found!")
        else:
            print("Updated successfully....")
    def delete_book(self):
        b_id=int(input("Enter the book id to delete: "))
        val=0
        for i in books:
            if i[0]==b_id:
                val=1
                books.remove(i)
        if val==0:
            print("Book not found!")
        else:
            print("Removed successfully..")
    def display_all_books(self):
        if len(books)==0:
            print("No books available!")
        else:
            print("All books available: ")
            for i in books:
                print("Book_id:",i[0])
                print("Book title:",i[1])
                print("Author:",i[2])
                print("Quantity:",i[3],"\n")
   
ad=Admin()
class User:
    def menu(self):
        while True:
            print("1.Registration\n2.Login\n3.Exit")
            n1=int(input("Enter your choice: "))
            if n1==1:
                self.registration()
            elif n1==2:
                self.login()
            elif n1==3:
                break
    def registration(self):
        name=input("Enter your name: ")
        age=int(input("Enter your age: "))
        address=input("Enter your address: ")
        number=input("Enter your number: ")
        val1=0
        for i in users:
            if i[3]==number:
                val1=1
                print("Phone number already exists!")
        if val1==0:
            u_name=input("Enter your username: ")
            val=0
            for i in users:
                if i[4]==u_name:
                    val=1
                    print("Username already exists!")
            if val==0:
                pas=input("Enter your password: ")
                l=[name,age,address,number,u_name,pas]
                users.append(l)
    def login(self):
        us_name=input("Enter your username: ")
        l_pas=input("Enter your password: ")
        val=0
        for i in users:
            if i[4]==us_name and i[5]==l_pas:
                val=1
                while True:
                    print("User menu:")
                    print("1.Display All Books\n2.Search Book\n3.Exit")
                    ch=int(input("Enter your choice:"))
                    if ch==1:
                        ad.display_all_books()
                    elif ch==2:
                        self.search_book()
                    elif ch==3:
                        break
                    else:
                        print("Invalid choice!")
        if val==0:
            print("Invalid username or password!")
    def search_book(self):
        title=input("Enter the book title to search: ")
        val=0
        for i in books:
            if i[1]==title:
                val=1
                print("Book id:",i[0])
                print("Book title:",i[1])
                print("Author:",i[2])
                print("Quantity:",i[3])
        if val==0:
            print("Book not found!")

class MainMenu:
    while True:
        print("1.Admin\n2.User\n3.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            ad=Admin()
            ad.admin_login()
        elif ch==2:
            us=User()
            us.menu()
        elif ch==3:
            break
        else:
            print("Invalid choice!")

