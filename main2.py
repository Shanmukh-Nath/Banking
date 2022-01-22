import tkinter

root=tkinter.Tk()
e=tkinter.Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=10,padx=30)
list_of_numbers=[]

def number_inputs(number):
    current_value=e.get()
    e.delete(0, tkinter.END)
    e.insert(0,str(current_value)+str(number))

def clear_values():
    list_of_numbers.clear()
    e.delete(0, tkinter.END)
def summation():
    num1=e.get()
    list_of_numbers.append(num1)
    e.delete(0, tkinter.END)
    SUM=0
    for values in list_of_numbers:
        SUM+=int(values)
    return SUM
def equals():
    num1=e.get()
    list_of_numbers.append(int(num1))
    e.delete(0, tkinter.END)
    summation()
    e.insert(0,str(SUM))
def subtraction():



#buttons
buttn9=tkinter.Button(root,text="9",padx=40,pady=20,command=lambda : number_inputs(9)).grid(row=1,column=0)
buttn8=tkinter.Button(root,text="8",padx=40,pady=20,command=lambda : number_inputs(8)).grid(row=1,column=1)
buttn7=tkinter.Button(root,text="7",padx=40,pady=20,command=lambda : number_inputs(7)).grid(row=1,column=2)
buttn6=tkinter.Button(root,text="6",padx=40,pady=20,command=lambda : number_inputs(6)).grid(row=2,column=0)
buttn5=tkinter.Button(root,text="5",padx=40,pady=20,command=lambda : number_inputs(5)).grid(row=2,column=1)
buttn4=tkinter.Button(root,text="4",padx=40,pady=20,command=lambda : number_inputs(4)).grid(row=2,column=2)
buttn3=tkinter.Button(root,text="3",padx=40,pady=20,command=lambda : number_inputs(3)).grid(row=3,column=0)
buttn2=tkinter.Button(root,text="2",padx=40,pady=20,command=lambda : number_inputs(2)).grid(row=3,column=1)
buttn1=tkinter.Button(root,text="1",padx=40,pady=20,command=lambda : number_inputs(1)).grid(row=3,column=2)
buttn0=tkinter.Button(root,text="0",padx=40,pady=20,command=lambda : number_inputs(0)).grid(row=4,column=0)
buttnadd=tkinter.Button(root,text="+",padx=40,pady=20,command=summation).grid(row=4,column=1)
buttnsub=tkinter.Button(root,text="-",padx=40,pady=20,command=).grid(row=4,column=2)
buttnmul=tkinter.Button(root,text="*",padx=40,pady=20,).grid(row=5,column=0)
buttndiv=tkinter.Button(root,text="/",padx=40,pady=20,).grid(row=5,column=1)
buttnequals=tkinter.Button(root,text="=",padx=40,pady=20,command=equals).grid(row=5,column=2)


root.mainloop()