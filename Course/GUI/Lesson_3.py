from tkinter import *
from window import *

root = Tk()
setwindow(root)

btn1 = Button(root,
              text="Моя кнопка",
              font="Tahoma 14",
              borderwidth=2,
              pady=5,
              padx=10,
              relief=RIDGE
              )
btn2 = Button(root,
              text="Моя кнопка",
              font="Tahoma 20",
              borderwidth=5,
              pady=5,
              padx=10,
              relief=RAISED
              )

btn1.pack(pady=10)
btn2.pack(pady=10)

root.mainloop()
