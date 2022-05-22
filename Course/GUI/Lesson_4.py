from tkinter import *
from window import *

root = Tk()
setwindow(root)

str_log = input("Enter string: ")

entry = Entry(root,
              font="Tahoma 20",
              bg="#fef2e4",
              fg="#805f3b"
              )
entry.insert(0, str_log)
entry.pack()

root.mainloop()
