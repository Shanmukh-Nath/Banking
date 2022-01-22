# Author = S.V. Shanmukh Nath
# Project Banking
# Started = 28-07-2021
# Version=0.01

import email
from email.message import EmailMessage
from http import server
from tkinter import *
import os
import random
from tkinter import messagebox
import smtplib
import itertools
import threading
from datetime import datetime
import sys
done = False
try:
    os.makedirs("C:\\Bank Details\\")
except:
    pass
root1 = Tk()
root1.iconbitmap(
    r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")


def accountgenerator():
    x = random.randint(1000000, 9999999)
    return x


def createfolder(anum):
    global directory
    directory = str(anum)
    parent_directory = "C:\\Bank Details"
    path = os.path.join(parent_directory, directory)
    os.mkdir(path)


class mainpage:

    def __init__(self, top=None):
        global rt
        top.geometry("800x700+50+50")
        top.title("Banking Software")
        self.root = root1
        rt = self.root
        bgR = PhotoImage(
            r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\mainpage.jpg")
        mylabel = Label(self.root, image=bgR)
        mylabel.place(x=0, y=0, relwidth=1, relheight=1)
        f1 = LabelFrame(self.root, bg="Black")
        f1.place(x=0, y=0, relwidth=1)
        l1 = Label(f1, text="Banking Software", font=(
            "arial", 15), fg="Yellow", bg="Black")
        l1.pack(fill=X)
        f2 = LabelFrame(self.root, text="Customer Details", font=(
            "times new roman", 14), fg="gold", bg="blue")
        f2.place(x=0, y=35, relwidth=1, relheight=1)
        btn1 = Button(f2, text="Existing Customer", command=(
            login), bg='white', font=("times new roman", 12), fg='red')
        btn1.grid(row=0, column=5, padx=300, pady=50)
        btn2 = Button(f2, text="New Customer", bg='white', command=(
            newcustomer), font=("times new roman", 12), fg='green')
        btn2.grid(row=5, column=5, pady=150)
        btn3 = Button(f2, text="Recent Info", bg="White",
                      font=("Times New Roman", 15), command=log)
        btn3.grid(row=6, column=5, pady=15)


Account_Number = StringVar()
Account_Name = StringVar()
Account_dob = StringVar()
Account_Mob = StringVar()
Account_email = StringVar()
Account_Address = StringVar()
Account_Aadhaar = StringVar()
Account_Pan = StringVar()
OTP1 = StringVar()
Account_Deposit = StringVar()
Withdraw = StringVar()
Deposit = StringVar()


def exit():
    nmin.destroy()
    bankingpage()


def withdrawinfo():
    num = Account_Number.get()
    w = int(Withdraw.get())
    f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "r")
    B = f.read()
    f.close
    b = int(B)
    if w > b:
        messagebox.showerror("Error", "Insufficient Funds.")
    else:
        R = b-w
        r = str(R)
        f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "w")
        f.write(f"{r}")
        f.close
        messagebox.showinfo("Info", "Your Withdrawal is Successful")
        messagebox.showinfo("Balance", f"Your Remaining Balance is Rs.{r}")
        exit()


def depositinfo():
    num = Account_Number.get()
    d = int(Deposit.get())
    f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "r")
    b = int(f.read())
    f.close
    r = d+b
    R = str(r)
    f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "w")
    f.write(f"{R}")
    f.close
    messagebox.showinfo("Info", "Your Deposit is Successful")
    messagebox.showinfo("Balance", f"Your Remaining Balance is Rs.{R}")
    infot = f"{num} Successfully Deposited."
    interlog(infot)
    exit()


def bankingpage():
    num = Account_Number.get()

    def withdraw():
        new.destroy()
        global nmin
        f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "r")
        money = f.read()
        f.close()
        nmin = Toplevel()
        nmin.geometry("900x700")
        nmin.iconbitmap(
            r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
        nmin.title("Withdraw Funds")
        f1 = LabelFrame(nmin, bg="Light Green")
        f1.place(x=0, y=0, relwidth=1)
        Toplbl = Label(f1, font=("arial", 20), text="Withdraw",
                       fg="Black", bg="Light Green")
        Toplbl.pack(fill=X)
        f2 = LabelFrame(nmin, bg="light yellow")
        f2.place(x=0, y=80, relwidth=1, relheight=1)
        currentlbl = Label(f2, font=("arial", 15),
                           text=f"Your Current Available Balance is Rs.{money}")
        currentlbl.grid(row=1, column=3, padx=50, pady=50)
        withdrawlbl = Label(f2, text="Withdraw", font=("arial", 15))
        withdrawlbl.grid(row=3, column=1, padx=50, pady=50)
        withdrawentry = Entry(f2, bd=3, font=(
            "arial", 10), textvariable=Withdraw)
        withdrawentry.grid(row=3, column=2, padx=50, pady=50)
        withdrawbtn = Button(f2, text="Submit", width=10,
                             command=(withdrawinfo))
        withdrawbtn.grid(row=5, column=3, padx=50, pady=50)

    def deposit():
        new.destroy()
        global nmin
        f = open(f"C:\\Bank Details\\{num}\\{num}.svs", "r")
        money = f.read()
        f.close()
        nmin = Toplevel()
        nmin.geometry("900x700")
        nmin.iconbitmap(
            r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
        nmin.title("Deposit Funds")
        f1 = LabelFrame(nmin, bg="Light Green")
        f1.place(x=0, y=0, relwidth=1)
        Toplbl = Label(f1, font=("arial", 20), text="Deposit",
                       fg="Black", bg="Light Green")
        Toplbl.pack(fill=X)
        f2 = LabelFrame(nmin, bg="light yellow")
        f2.place(x=0, y=80, relwidth=1, relheight=1)
        currentlbl = Label(f2, font=("arial", 15),
                           text=f"Your Current Available Balance is Rs.{money}")
        currentlbl.grid(row=1, column=3, padx=50, pady=50)
        depositlbl = Label(f2, text="Deposit (Rs.)", font=("arial", 15))
        depositlbl.grid(row=3, column=1, padx=50, pady=50)
        depositentry = Entry(f2, bd=3, font=(
            "arial", 10), textvariable=Deposit)
        depositentry.grid(row=3, column=2, padx=50, pady=50)
        depositbtn = Button(f2, text="Submit", width=10, command=(depositinfo))
        depositbtn.grid(row=5, column=3, padx=50, pady=50)

    def viewdetails():
        pass

    def changedetails():
        pass
    acs = Account_Number.get()
    f = open(f"C:\\Bank Details\\{acs}\\{acs} -name.svs", "r")
    nme = f.read()
    f.close()
    new = Toplevel()
    new.geometry("900x800")
    new.title("Banking Page")
    new.iconbitmap(
        r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
    f1 = LabelFrame(new)
    f1.place(x=0, y=0, relwidth=1, relheight=1)
    head_lbl = Label(f1, text=(f"Hi {nme},\n\t\tWelcome to our Banking Services."),
                     bg="black", fg="Yellow", font=("arial black", 20))
    head_lbl.pack(fill=X)
    f2 = LabelFrame(new, bg="pink")
    f2.place(x=0, y=80, relwidth=1, height=700)
    withdraw_btn = Button(f2, text="Withdraw", font=(
        "arial", 15), command=withdraw, fg="Green", width=30)
    withdraw_btn.grid(row=2, column=1, padx=50, pady=50)
    deposit_btn = Button(f2, text="Deposit", font=(
        "arial", 15), command=deposit, fg="red", width=30)
    deposit_btn.grid(row=4, column=1, padx=50, pady=50)
    balance_btn = Button(f2, text="View Balance", font=(
        "arial", 15), fg="Green", width=30)
    balance_btn.grid(row=6, column=1, padx=50, pady=50)
    viewdetails_btn = Button(f2, text="View Details",
                             font=("arial", 15), fg="Green", width=30)
    viewdetails_btn.grid(row=2, column=3, padx=50, pady=50)
    logged = f"{acs} Successfully Logged in."
    interlog(logged)


def email_send(acc):
    msg = EmailMessage()
    msg.set_content(str(otp)+' This is your OTP To Login.')
    msg['Subject'] = 'OTP To Login.'
    msg['From'] = "donotreplythisisotp@gmail.com"
    f = open(f"C:\\Bank Details\\{acc}\\{acc} -email.svs", "r")
    emailid = f.read()
    f.close
    msg['To'] = emailid
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("donotreplythisisotp@gmail.com", "9492561643")
    server.send_message(msg)
    server.quit()
    sent = f"Email Successfully Sent to {acc} with otp "+str(otp)
    interlog(sent)


def resend():
    asc = Account_Number.get()
    msg = EmailMessage()
    msg.set_content(str(otp2)+' This is your OTP To Login.')
    msg['Subject'] = 'OTP To Login.'
    msg['From'] = "donotreplythisisotp@gmail.com"
    f = open(f"C:\\Bank Details\\{asc}\\{asc} -email.svs", "r")
    emailid = f.read()
    f.close
    msg['To'] = emailid
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("donotreplythisisotp@gmail.com", "9492561643")
    server.send_message(msg)
    server.quit()
    sent = f"Email Successfully Sent to {asc} with otp "+str(otp2)
    interlog(sent)


def interlog(sent, logged, infot):
    pass


def log():
    nwen = Toplevel()
    nwen.geometry("600x400")
    nwen.title("Recent Info")
    l = Label(nwen, text="Log Files\n")
    l.config(font=("times new roman", 14))
    l.pack()


def logged(acc, name, now):
    msg = EmailMessage()
    msg.set_content(
        f"User {name} with Account Number {acc} has logged in at {now}.\n If this is not you Please Reply to this Email.")
    msg['Subject'] = f'User {name} Logged in.'
    msg['From'] = "donotreplythisisotp@gmail.com"
    f = open(f"C:\\Bank Details\\{acc}\\{acc} -email.svs", "r")
    emailid = f.read()
    f.close
    msg['To'] = emailid
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("donotreplythisisotp@gmail.com", "9492561643")
    server.send_message(msg)
    server.quit()


def otppage(acc):
    global otp, otp2
    otp = random.randint(100000, 999999)
    otp2 = random.randint(100000, 999999)

    def checkotp():
        n = "None"
        intotp = int(OTP1.get())
        if intotp == otp or intotp == otp2:
            messagebox.showinfo("Successful", "Your Login is Successful.")
            asc = Account_Number.get()
            f = open(f"C:\\Bank Details\\{asc}\\{asc} -email.svs", "r")
            emailid = f.read()
            f.close()
            f = open(f"C:\\Bank Details\\{asc}\\{asc} -name.svs", "r")
            name = f.read()
            f.close()
            now = datetime.now()
            logged(asc, name, now)
            n = "done"
            win.destroy()
            bankingpage()
            logged1 = f"User {name} has logged in with account number {asc} with email {emailid}."
            interlog(logged1)
        elif(n == "done"):
            messagebox.showinfo("Info", "Sorry you are already Logged in.")
        else:
            messagebox.showwarning("Error", "Wrong OTP.")
    win = Toplevel()
    win.geometry("800x600")
    win.title("Login with OTP")
    win.iconbitmap(
        r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
    f1 = LabelFrame(win)
    f1.place(x=0, y=0, relwidth=1)
    nw_title = Label(f1, text="Verify OTP to Login", bg="red",
                     font=("arial black", 20, "bold"))
    nw_title.pack(fill=X)
    f2 = LabelFrame(win)
    f2.place(x=0, y=45, relwidth=1, relheight=1)
    f = open(f"C:\\Bank Details\\{acc}\\{acc} -email.svs", "r")
    email = f.read()
    f.close()
    acc_lbl = Label(f2, text=f"Enter OTP Sent to {email}", font=("arial", 12))
    acc_lbl.grid(row=1, column=0, padx=50, pady=50)
    acc_entry = Entry(f2, bd=3, textvariable=OTP1, relief=SUNKEN)
    acc_entry.grid(row=1, column=1)
    submit_btn = Button(f2, text="Submit OTP", command=(
        checkotp), bd=3, fg="green", font=("arial", 14), width=10)
    submit_btn.grid(row=2, column=1, padx=50, pady=50)
    resend_btn = Button(f2, text="Resend OTP", command=(
        resend), bd=3, fg="red", font=("arial", 14), width=10)
    resend_btn.grid(row=3, column=1, padx=50, pady=50)


def login():
    global nw
    nw = Toplevel()
    nw.geometry("620x500")
    nw.title("Existing Customer")
    nw.iconbitmap(
        r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
    f1 = LabelFrame(nw)
    f1.place(x=0, y=0, relwidth=1)
    nw_title = Label(f1, text="Existing Customer", bg="lime",
                     font=("arial black", 20, "bold"))
    nw_title.pack(fill=X)
    f2 = LabelFrame(nw)
    f2.place(x=0, y=45, relwidth=1, relheight=1)
    acc_lbl = Label(f2, text="Account Number", font=("arial", 12))
    acc_lbl.grid(row=1, column=0, padx=50, pady=50)
    acc_entry = Entry(f2, bd=3, textvariable=Account_Number, relief=SUNKEN)
    acc_entry.grid(row=1, column=1)
    submit_btn = Button(f2, text="Submit", command=(
        submitdata), bd=3, fg="green", font=("arial", 14), width=10)
    submit_btn.grid(row=2, column=1, padx=50, pady=50)


def newcustomer():
    def clicker(event):
        mlabel = Label(nwin)
        mlabel.pack()
        checkdetails()
    global nwin
    nwin = Toplevel()
    nwin.geometry("720x600")
    nwin.title("New Customer")
    nwin.iconbitmap(
        r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
    f1 = LabelFrame(nwin)
    f1.place(x=0, y=0, relwidth=1)
    nw_title = Label(f1, text="New Customer", bg="lime",
                     font=("arial black", 20, "bold"))
    nw_title.pack(fill=X)
    y = accountgenerator()
    f2 = LabelFrame(nwin)
    f2.place(x=0, y=45, relwidth=1, relheight=1)
    acc_n = Label(f2, text="Full Name", font=("arial", 12))
    acc_n.grid(row=0, column=0, padx=5, pady=5)
    acc_n1 = Label(f2, text="Mobile Number", font=("arial", 12))
    acc_n1.grid(row=1, column=0, padx=5, pady=5)
    acc_n2 = Label(f2, text="Email", font=("arial", 12))
    acc_n2.grid(row=2, column=0, padx=5, pady=5)
    acc_n3 = Label(f2, text="Date Of Birth", font=("arial", 12))
    acc_n3.grid(row=3, column=0, padx=5, pady=5)
    acc_n3 = Label(f2, text="Aadhaar Number", font=("arial", 12))
    acc_n3.grid(row=0, column=2, padx=5, pady=5)
    acc_n3 = Label(f2, text="PAN Number", font=("arial", 12))
    acc_n3.grid(row=1, column=2, padx=5, pady=5)
    acc_n3 = Label(f2, text="Address", font=("arial", 12))
    acc_n3.grid(row=2, column=2, padx=5, pady=5)
    # Entry
    acc_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Name)
    acc_en.grid(row=0, column=1, padx=5, pady=5)
    acc1_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Mob)
    acc1_en.grid(row=1, column=1, padx=5, pady=5)
    acc2_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_email)
    acc2_en.grid(row=2, column=1, padx=5, pady=5)
    acc3_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_dob)
    acc3_en.grid(row=3, column=1, padx=5, pady=5)
    acc4_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Aadhaar)
    acc4_en.grid(row=0, column=3, padx=5, pady=5)
    acc5_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Pan)
    acc5_en.grid(row=1, column=3, padx=5, pady=5)
    acc5_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Address)
    acc5_en.grid(row=2, column=3, padx=5, pady=5)

    submit_btn = Button(f2, text="Submit", bd=3, fg="green", font=(
        "arial", 14), width=10, command=checkdetails)
    submit_btn.bind("<Return>", clicker)
    submit_btn.grid(row=4, column=1, padx=50, pady=50)


def initialdeposit():
    global win
    win = Toplevel()
    win.geometry("800x400")
    win.title("Initial Deposit")
    win.iconbitmap(
        r"C:\Users\shanm\OneDrive\Desktop\My projects\Banking\icon.ico")
    f1 = LabelFrame(win)
    f1.place(x=0, y=0, relwidth=1)
    top_title = Label(f1, text="Initial Deposit", font=(
        "arial", 15), bg="Black", fg="Yellow")
    top_title.pack(fill=X)
    f2 = LabelFrame(win)
    f2.place(x=0, y=50, relwidth=1)
    # label
    dp_lbl = Label(f2, text="Deposit Amount(Rs.)", font=("arial", 9))
    dp_lbl.grid(row=2, column=0, padx=5, pady=5)
    # Entry
    dp_en = Entry(f2, bd=3, font=("arial", 10), textvariable=Account_Deposit)
    dp_en.grid(row=2, column=3, padx=5, pady=5)
    # Button
    dp_btn = Button(f2, text="Submit", font=("arial", 10), command=(newsubmit))
    dp_btn.grid(row=6, column=3, padx=5, pady=5)


def checkdetails():
    nwin.destroy()
    anum = accountgenerator()
    aname = Account_Name.get()
    amob = Account_Mob.get()
    aemail = Account_email.get()
    adob = Account_dob.get()
    aadh = Account_Aadhaar.get()
    apan = Account_Pan.get()
    add = Account_Address.get()
    if aname == "" or amob == "" or aemail == "" or adob == "" or aadh == "" or apan == "" or add == "":
        messagebox.showerror(
            "Error", "You have not entered all the deatils required.")
        q = messagebox.askyesno("Info", "Would you like to retry the form.")
        if(q == YES):
            newcustomer()
        elif(q == NO):
            root1.destroy()
    else:
        inter()


def inter():
    anum = accountgenerator()
    aname = Account_Name.get()
    amob = Account_Mob.get()
    aemail = Account_email.get()
    adob = Account_dob.get()
    aadh = Account_Aadhaar.get()
    apan = Account_Pan.get()
    add = Account_Address.get()
    ques = messagebox.askyesno(
        "Deposit", "TO Successfully create your account, please Deposit Some funds to your new account.")
    if(ques == YES):
        initialdeposit()
    else:
        msg = messagebox.showinfo(
            "Wrong Path", "If you cannot Deposit Initial Funds, we cannot create your account, please retry and fill the form again.\n\t\t Thank you.")
        root1.destroy()


def newsubmit():
    win.destroy()
    dp = Account_Deposit.get()
    anum = accountgenerator()
    aname = Account_Name.get()
    amob = Account_Mob.get()
    aemail = Account_email.get()
    adob = Account_dob.get()
    aadh = Account_Aadhaar.get()
    apan = Account_Pan.get()
    add = Account_Address.get()
    createfolder(anum)
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -name.svs", "w")
    f.write(f"{aname}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -dob.svs", "w")
    f.write(f"{adob}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -mobile.svs", "w")
    f.write(f"{amob}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -email.svs", "w")
    f.write(f"{aemail}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -aadhaar.svs", "w")
    f.write(f"{aadh}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -pan.svs", "w")
    f.write(f"{apan}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -address.svs", "w")
    f.write(f"{add}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum} -account number.svs", "w")
    f.write(f"{anum}")
    f.close()
    f = open(f"C:\\Bank Details\\{anum}\\{anum}.svs", "w")
    f.write(f"{dp}")
    f.close
    messagebox.showinfo("Info", f"Your Account {anum} Successfully Created.")


def submitdata():
    nw.destroy()
    acc = Account_Number.get()
    f = open(f"C:\\Bank Details\\{acc}\\{acc} -account number.svs", "r")
    acc_r = f.read()
    f.close()
    if (acc) == (acc_r):
        messagebox.showinfo("Info", "Success Your Account Data is Validated.")
        otppage(acc)
        email_send(acc)
    else:
        messagebox.showerror("Error", "Invalid Account Number")


page1 = mainpage(root1)
root1.mainloop()
