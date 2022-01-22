from tkinter import *
ws = Tk()
ws.title('PythonGuides')
ws.geometry('800x600')
ws.config(bg='yellow')

img = PhotoImage(
    r"C:\\Users\shanm\\OneDrive\Desktop\\My projects\Banking\\mainpage.jpg")
label = Label(
    ws,
    image=img
)
label.place(x=0, y=0)

text = Text(
    ws,
    height=10,
    width=53
)
text.place(x=30, y=50)

button = Button(
    ws,
    text='SEND',
    relief=RAISED,
    font=('Arial Bold', 18)
)
button.place(x=190, y=250)

ws.mainloop()
