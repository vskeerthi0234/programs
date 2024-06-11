#write a program to bulid a login system using functions.The function name should be login and register-
#>>>first it shld ask user to enter the details for the registeration and out of all these details nly username n passwrod should be stored
# now this function shld ask user to enter user name n password.if these match with the registered details login success else repeat this login process  
#saying inavlid credentials

users={}
def register():
    reg_username=input("enter your name")
    reg_password=input("enter a passwrord")
    if reg_username in users:
        print("user alread exists")
    else:
        print("register successful")
def login():
    username=input("enter your name")
    password=input("enter a passwrord")
    if username in users and password==password:
        print("login successfull")
    else:
        login()
        print("invalid credentials")
def main():
    while True:
        print("1.register \n 2. login \n 3.exit")
        ch=int(input("enter your choice"))
        if ch==1:
            register()
        elif ch==2:
            login()
        elif ch==3:
            exit()
        else:
            print("invalid choice")
main()