from tkinter import *
from window import *
from random import *

root = Tk()
setwindow(root)

choice1 = StringVar()
choice2 = StringVar()
check1 = Checkbutton(root, text="Согласие на обработку данных", variable=choice1, onvalue="Yes", offvalue="No")
check2 = Checkbutton(root, text="Согласие на обработку данных", variable=choice2, onvalue="Yes", offvalue="No")

check1.pack()
check2.pack()

choice1.set("No")
choice2.set("Yes")

root.mainloop()