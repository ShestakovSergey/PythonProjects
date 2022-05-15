from tkinter import *
from window import *

root = Tk()
setwindow(root)


label_author = Label(root, text="Authorization", font="Tahoma 20", borderwidth=1, relief="solid")
label_login = Label(root, text="Login", font="Tahoma 20", borderwidth=1, relief="solid")
entry_login = Entry(root, font="Tahoma 20", borderwidth=1, relief="solid")
label_passwd = Label(root, text="Password", font="Tahoma 20", borderwidth=1, relief="solid")
entry_passwd = Entry(root, font="Tahoma 20", borderwidth=1, relief="solid", show="*")
button = Button(text="Enter", font="Tahoma 20", borderwidth=1, relief="raised")

label_author.grid(row=0, column=0, columnspan=2, sticky="nw", padx=5, pady=5)
label_login.grid(row=1, column=0, sticky="w", pady=5, padx=5)
entry_login.grid(row=1, column=1, sticky="w", pady=5, padx=5)
label_passwd.grid(row=2, column=0, sticky="w", pady=5, padx=5)
entry_passwd.grid(row=2, column=1, sticky="w", pady=5, padx=5)
button.grid(row=3, column=0, columnspan=2, sticky="se", padx=5, pady=5)

root.mainloop()