from tkinter import *
from window import *
from random import *

root = Tk()
setwindow(root)

numb = int(random() * 100)

label = Label(root, text=numb)

label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
