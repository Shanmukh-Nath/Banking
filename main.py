import tkinter as Tk
import os
import random
global number
try:
    os.makedirs("C:\\Bank Details")
except:
    pass    
def viewdetails(acc_number):
    inp=int(input("\n<----------------------------->Choose What Detail to View.<------------------------------>\n1.Name\n2.Date of Birth\n3.Account Number\n4.Card Pin\n\t\t\t\t :"))
    if(inp==1):
        f=open("C:\\Bank Details\\{}\\{} -name.svs".format(acc_number,acc_number),"r")
        n=f.read()
        f.close()
        print("Your Name Registered with us is "+n)
    elif(inp==2):
        f = open("C:\\Bank Details\\{}\\{} -dob.svs".format(acc_number, acc_number), "r")
        d=f.read()
        f.close()
        print("Your Date of Birth Registered with us is "+ d)
    elif(inp==3):
        print("Your Account Number is {}".format(acc_number))
    elif(inp==4):
        f = open("C:\\Bank Details\\{}\\{} -code.svs".format(acc_number, acc_number), "r")
        c=f.read()
        f.close()
        print("Your ATM Secret Key is {}".format(c))
    else:
        print("Invalid Choice.")
        exit(4)


def account_generator():
    new_account=random.randint(192300001,192400000)
    return new_account
def createfolder(new_account):
    global directory
    directory=str(new_account)
    parent_directory="C:\\Bank Details"
    path=os.path.join(parent_directory,directory)
    os.mkdir(path)

def withdraw(acc_number):
    global money_account
    f=open("C:\\Bank Details\\{}\\{}.svs".format(acc_number,acc_number),"r")
    money=f.read()
    f.close()
    print("Available Balance in the account = Rs.{}".format(money))
    withdrawal =input("Enter the amount to Withdraw. : ")
    if withdrawal <= money:
        print("Amount Withdrawn in currency notes.")
        print(currencycount(withdrawal))
        print("Successful Transaction.")
        print("Amount has been withdrawn.")
        print("Please Collect cash from Cash Dispencer.")
        updated_withdrawal = (int(money) - int(withdrawal))
        f=open("C:\\Bank Details\\{}\\{}.svs".format(acc_number,acc_number),"w")
        f.write("{0}".format(updated_withdrawal))
        f.close()
        print("Available balance = Rs.{}".format(updated_withdrawal))
    else:
        print("Insufficient Funds to Withdraw.")
        exit(2)

def code():
    pin_code=int(input("Set a Code for your ATM Transactions : "))
    return pin_code


def deposit(acc_number):
    global money_account
    deposit_cash = input("\n\nEnter the Amount to be Deposited. : ")
    f=open("C:\\Bank Details\\{}\\{}.svs".format(acc_number,acc_number),"r")
    money_account = f.read()
    f.close()
    money_deposit = (int(money_account) + int(deposit_cash))
    print("Successful Transaction.")
    print("Available balance in your Account = Rs.{}".format(money_deposit))
    f=open("C:\\Bank Details\\{}\\{}.svs".format(acc_number,acc_number),"w")
    f.write("{0}".format(money_deposit))
    f.close()

def Balance_Enquiry(acc_number):
    f=open("C:\\Bank Details\\{}\\{}.svs".format(acc_number,acc_number),"r")
    balance=f.read()
    f.close()
    print("\n\nFunds Available in your account = Rs.{}".format(balance))

def currencycount(withdrawal):
    notes = [2000, 500, 200, 100]

    noteCounter = [0, 0, 0, 0]

    print("Currency Count.\n ")

    for i, j in zip(notes, noteCounter):
        if int(withdrawal) >= i:
            j = int(withdrawal) // i
            withdrawal = int(withdrawal) - j * i
            print(i, " x ", j)
def new_bank_account():
    global fullname,dob
    fullname=input("Enter your Full Name :")
    dob=input("Enter your Date of Birth(DD-MM-YYYY):")
    account_number=account_generator()
    createfile(account_number)

def changedetails(acc_number):
    ip=input("\n**********************************####Choose which Detail you want to change.#####***********************************\n1.Name\n2.Date of Birth\n3.Code\n\t\t\t\t :")
    if(ip==1):
        new_name=input("Enter your Name : ")
        f=open("C:\\Bank Details\\{}\\{} -name.svs".format(acc_number,acc_number),"w")
        f.write(new_name)
        f.close()
        print("Your Name is Successfully Updated.")
    elif(ip==2):
        new_dob=input("Enter your Date of Birth : ")
        f=open("C:\\Bank Details\\{}\\{} -dob.svs".format(acc_number,acc_number),"w")
        f.write(new_dob)
        f.close()
        print("Your Date of Birth is Successfully Updated.")
    elif(ip==3):
        new_code=input("Enter the Code : ")
        f=open("C:\\Bank Details\\{}\\{} -code.svs".format(acc_number,acc_number),"w")
        f.write(new_code)
        f.close()
        print("Your Code is Successfully Changed.")
    else:
        print("Invalid Choice.")
        exit(1)

def createfile(account_number):
    createfolder(account_number)
    f=open("C:\\Bank Details\\{}\\{} -name.svs".format(directory,account_number),"w")
    f.write(fullname)
    f.close()
    f=open("C:\\Bank Details\\{}\\{} -dob.svs".format(directory,account_number),"w")
    f.write(dob)
    f.close()
    f=open("C:\\Bank Details\\{}\\{}.svs".format(directory,account_number),"w")
    f.write("0")
    f.close()
    f=open("C:\\Bank Details\\{}\\{} -code.svs".format(directory,account_number),"w")
    key=code()
    f.write("{}".format(key))
    f.close()
    print("Successfully New Account Created.")
    print("Please Note your Account Number = {}".format(account_number))
def ExistingCustomer():
    root1=Tk.Tk()
    L0=Tk.Label(root1,text="Existing Customer.",)
    L0.grid(row=0,column=5)
    L1=Tk.Label(root1,text="Account Number",)
    L1.grid(row=1,column=0)
    E1=Tk.Entry(root1,bd=5)
    E1.grid(row=1,column=1)
    B=Tk.Button(root1,text="Submit")
    B.pack()
    B.grid(row=2,column=5)
    root1.mainloop()


root=Tk.Tk()
button=Tk.Button(root,text="Exitsing Customer",command=ExistingCustomer()).grid(row=2,column=2)

root.mainloop()