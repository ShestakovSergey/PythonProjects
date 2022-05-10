from tkinter import *
from window import *
from random import *

root = Tk()
setwindow(root)

choice = IntVar()
check = Checkbutton(root, text="Согласие на обработку данных", variable=choice, onvalue=1, offvalue=0)
#check.select()
check.pack()

numb = 1 if int(random() * 10) > 4 else 0
choice.set(numb)

label = Label(root, text=choice.get())
label.pack()

print(choice.get())

root.mainloop()