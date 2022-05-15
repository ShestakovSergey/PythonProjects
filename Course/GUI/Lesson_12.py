from tkinter import *
from window import *

root = Tk()
setwindow(root)


label_author = Label(root, text="Authorization", font="Tahoma 20", borderwidth=1, relief="solid")
label_login = Label(root, text="Login", font="Tahoma 20", borderwidth=1, relief="solid")
entry_login = Entry(root, font="Tahoma 20", borderwidth=1, relief="solid")
label_passwd = Label(root, text="Password", font="Tahoma 20", borderwidth=1, relief="solid")
entry_passwd = Entry(root, font="Tahoma 20", borderwidth=1, relief="solid")
button = Button(text="Enter", font="Tahoma 20", borderwidth=1, relief="raised")


label_author.place(x=0, y=0, width=600, height=50, anchor="nw")
label_login.place(x=0, y=50, width=200, height=50, anchor="nw")
entry_login.place(x=200, y=50, width=400, height=50, anchor="nw")
label_passwd.place(x=0, y=100, width=200, height=50, anchor="nw")
entry_passwd.place(x=200, y=100, width=400, height=50, anchor="nw")
button.place(x=0, y=150, width=600, height=50, anchor="nw")

root.mainloop()