from tkinter import *
from window import *
from random import *

root = Tk()
setwindow(root)

numb = int(random() * 1000)

label = Label(root,
              text=numb,
              font="Tahoma 20",
              fg="#FF0000",
              bg="#98FB98"
              )

label.pack()

root.mainloop()
