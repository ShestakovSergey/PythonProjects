from tkinter import *
from tkinter import messagebox
from window import *

root = Tk()
setwindow(root)

def show_message():
    messagebox.showinfo("GUI Python", message.get())

message = StringVar()

mess_entry = Entry(textvariable=message)
mess_entry.place(relx=.5, rely=.1, anchor="center")

mess_btn = Button(text="Click me", command=show_message)
mess_btn.place(relx=.5, rely=.5, anchor="center")


root.mainloop()
