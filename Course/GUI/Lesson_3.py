from tkinter import *
from window import *

root = Tk()
setwindow(root)

button1 = Button(root, text="Моя кнопка", bg="red", fg="black", font="Tahoma 18")
button2 = Button(root, text="Моя кнопка", bg="yellow", fg="black", font="Tahoma 20")

button1.pack()
button2.pack()

root.mainloop()
