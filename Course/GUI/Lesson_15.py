from tkinter import *
from random import *
from window import *

root = Tk()
setwindow(root)


def btn_clk(event):
    lbl['text'] = "Randon number {0}".format(int(random() * 100))


btn = Button(root,
              text="Ask",
              font="Tahoma 14",
              borderwidth=2,
              pady=5,
              padx=10,
              relief=RAISED
              )

lbl = Label(root,
              text="Randon number",
              font="Tahoma 14",
              borderwidth=2,
              pady=5,
              padx=10,
              relief=RIDGE
              )

btn.bind("<Button-1>", btn_clk)

btn.pack(pady=10)
lbl.pack(pady=10)

root.mainloop()
