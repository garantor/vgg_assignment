"""
Build a command-line Banking Application with the following functionalities:
 Application starts with a prompt to the user with the following options:
Press 1: create account
Press 2: transaction

2. Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account

3. Transaction: Authenticate the user by prompting for a password, if the password is correct, user is authenticated and show the following options:
Press 1: check balance
Press 2: withdraw
Press 3: transfer
if the password is incorrect, tell the user that they are not authorized and go back to the create account option

4. check balance: query your data structure to check the balance of the authenticated user

Build a command-line Banking Application with the following functionalities:
 Application starts with a prompt to the user with the following options:
Press 1: create account
Press 2: transaction

2. Create account: This should prompt you to enter an email/or unique identity, and then a password. You must check your data structure to make sure the account is unique before creating the new account.[Hint: Ensure that you data structure caters for each users account balance, you might want to initialize this to 0.0]

3. Transaction: Authenticate the user by prompting for a password, if the password is correct, user is authenticated and show the following options:
Press 1: check balance
Press 2: deposit
Press 3: withdraw
Press 4: transfer
if the password is incorrect, tell the user that they are not authorized and go back to the create account option

4. check balance: query your data structure to check the balance of the authenticated user

5. deposit: prompt the user to enter an amount, then add the amount to the users balance

6. withdraw: prompt the user to enter an amount, if the user does not have money in their account, tell them to deposit and move to the deposit prompt. If they user has money, print out the amount withdrawn and the available balance,

7. transfer: prompt the user to enter an email of the person they want to transfer to, prompt for the amount, deduct the amount from the authenticated users balance, add the amount to the beneficiaries account,

Ensure that you clog all the gaps for those process flows that i have not explicitly defined

"""

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

    
