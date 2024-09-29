admin_details={"Username":"a","Password":"1"}
product_details=[]


p_id=1
def add_product():
    d={}
    global p_id
    print("Add new product:")
    print("Product id:",p_id)
    name=input("Enter the name of the product: ")
    des=input("Enter the description: ")
    price=int(input("Enter the price: "))
    d["Product_id"]=p_id
    d["Name"]=name
    d["Description"]=des
    d["Price"]=price
    product_details.append(d)
    p_id+=1
def update_product():
    id=int(input("Enter the product id to update: "))
    val=0
    for i in product_details:
        if i["Product_id"]==id:
            val=1
            while True:
                print("What to update: ")
                print("1.Name\n2.Description\n3.Price\n4.Exit")
                n=int(input("Enter Your choice: "))
                if n==1:
                    name=input("Enter new name: ")
                    i["Name"]=name
                elif n==2:
                    des=input("Enter new description: ")
                    i["Description"]=des
                elif n==3:
                    price=int(input("Enter new price: "))
                    i["Price"]=price
                elif n==4:
                    break
                else:
                    price("Invalid choice!")
    if val==0:
        price("Id not found!")

def remove_product():
    id=int(input("Enter the product id to remove: "))
    val=0
    for i in product_details:
        if i["Product_id"]==id:
            val=1
            product_details.remove(i)
            print("Removed Successfully....")
    if val==0:
        print("Id not found!")

def view_all_products():
    if len(product_details)==0:
        print("No Products available!")
    else:
        print("All products available:")
        for i in product_details:
            print(i)

def view_orders():
    if len(orders)==0:
        print("No orders placed!")
    else:
        for i in orders:
            print("Product",i["Product"])
            print("Quantity:",i["Quantity"])
            print("Order status:",i["Order status"],"\n")


def admin():
    u_name=input("Enter the username: ")
    pas=input("Enter the password: ")
    if u_name==admin_details["Username"] and pas==admin_details["Password"]:
        while True:
            print("ADMIN MENU:")
            print("1.Add product\n2.Update product\n3.Remove product\n4.View all products\n5.View orders\n6.Exit")
            n=int(input("Enter your choice: "))
            if n==1:
                add_product()
            elif n==2:
                update_product()
            elif n==3:
                remove_product()
            elif n==4:
                view_all_products()
            elif n==5:
                view_orders()
            elif n==6:
                print("Exit from admin menu!")
                break
            else:
                print("Invalid choice!")

    else:
        print("Invalid username or password!")


user_list=[]
def register():
    d={}
    u_id=input("Enter user_id: ")
    for i in user_list:
        if i["User_id"]==u_id:
            print("User_id already exists!\nTry another.")
            register()
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")
    pas=input("Enter password: ")
    d["User_id"]=u_id
    d["Name"]=name
    d["Email"]=email
    d["Address"]=address
    d["Password"]=pas
    user_list.append(d)
    

orders=[]
def place_order(i):
    d={}
    view_all_products()
    pro=int(input("Enter the product id to place order: "))
    quantity=int(input("Enter the quantity: "))
    for j in product_details:
        if j["Product_id"]==pro:
            d["Product Name"]=j["Name"]
    d["Product"]=pro
    d["Quantity"]=quantity
    d["Order status"]="Processing"
    d["User Name"]=i["Name"]
    d["User_id"]=i["User_id"]
    orders.append(d)
    print("Order placed.......")
    
def view_order_history(i):
    val=0
    for j in orders:
        if j["User_id"]==i["User_id"]:
            val=1
            print("Product Name: ",j["Product Name"])
            print("Quantity:",j["Quantity"])
            print("Order Status:",j["Order status"],"\n")
    if val==0:
        print("No orders placed!")


def login():
    u_name=input("Enter user_id: ")
    pas=input("Enter password")
    for i in user_list:
        if i["User_id"]==u_name and i["Password"]==pas:
            while True:
                print("\nUSER MENU:")
                print("1.View All Products\n2.Place Order\n3.View Order History\n4.Exit")
                n=int(input("Enter your choice: "))
                if n==1:
                    view_all_products()
                elif n==2:
                    place_order(i)
                elif n==3:
                    view_order_history(i)
                elif n==4:
                    print("Exit from User menu!")
                    break
                else:
                    print("Invalid Choice!")

def user():
    while True:
        print("USER MENU:")
        print("1.Register\n2.Login\n3.Exit")
        n=int(input("Enter your choice: "))
        if n==1:
            register()
        elif n==2:
            login()
        elif n==3:
            print("Exit from user menu!")
            break
        else:
            print("Invalid choice!")


while True:
    print("MAIN MENU:")
    print("1.Admin\n2.User\n3.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        admin()
    elif ch==2:
        user()
    elif ch==3:
        print("Exit!!")
        break
    else:
        print("Invalid choice!")