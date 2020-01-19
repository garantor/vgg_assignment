

a=("Welcome to Vgg Microfinance bank")


customer={}
bal = 0.0
b = []


def create_account():
    email = input("Please enter your email: ")
    password = input("Please Enter the password of your Choice: ")
    if email not in b :
        c = b.insert(0, email)
        d = b.insert(1, password)
        e = b.insert(2, bal)
        print(" Email Added")
        return Transaction()
        
        
    else:
        print("email already exist")
        

def Transaction():
    print(b)
    password = input("Please Enter Your Password: ")
    email = input(" please Enter Your email: ")
    passw = (b[1])
    print(passw)
    if password == passw:
        print('Press 1: To Check Balance \nPress 2: Deposit \nPress 3: Withdrawal \nPress 4: To Transfer')
        choice = input('Enter Your Choice: ')
        if choice == '1':
            return check_balance()
        elif choice == '2':
            return deposit()
            
        elif choice == '3':
            withdraw()
            
        elif choice == '4':
            transfer()
            
        elif choice == ' ':
            print('Enter a Valid Choice ')
            return Transaction(email)
        else:
            print('Invalid Entry')
    else:
        print("You are not authorized to login")
        return create_account()
        
def check_balance():
    print('Your Bal is : ' + str(b[2]))
    return welcome()
        
        
        
def deposit():
    password = input("Please Enter Your Password: ")
    email = input(" please Enter Your email: ")
    amt = int(input("please Enter amount to deposit : "))
    oldbal = b[2]    
    newbal = int(oldbal) + amt
    b[2] = newbal
    print('Weldone, ' + str(amt) + ' has been added to your account \nYour new is ' + str(newbal))
    return welcome()
    
def withdraw():
    amt = int(input("Please Enter amount to withdraw : "))
    
    if amt >= b[2]:
        print(" You dont have enough bal to withdraw, please make a deposit ")
        return deposit()
    else:
        newb = b[2] - int(amt)
        b[2]=newb
        print("You Just withdraw " + str(amt) + "\nYour new bal is now " + str(newb))
        return welcome()
    
        
def welcome(): 

    print(a.upper())
    print("Please Enter Your Choice, \n1. Create an Account \n2. Transaction \n0 Exit")
    choice = input("Enter: ")
    if choice == str(1):
        create_account()
    elif choice == str(2):
        Transaction()
        
    elif choice == '0':
        quit()
      
    else:
        print('Invalid Entry')
        return welcome()
        
        
def transfer():
    amt=int(input("amount to send to user: "))
    email = input("Enter Email of Recipient :")
    if amt >= b[2]:
        print("You cant send that amount please Choose a lower bal" )
    elif amt == ' ':
        print("Please Enter a value ")
        return transfer()
    else:
        newbalance = b[2] -amt
        print(str(amt) + " has been sent \nYour new bal is now " +str(newbalance))
        
welcome()

    
