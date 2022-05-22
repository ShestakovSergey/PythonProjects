from tkinter import *
from random import *
from window import *

root = Tk()
setwindow(root)


def handlerenter(event):
    event.widget.config(bg='#ff0000', activebackground='#ff0000')


def handlerleave(event):
    event.widget.config(bg='#ffff7f')


def handlerclk(event):
    event.widget.config(bg='#ccff00', activebackground='#ccff00')


def entermouse(event):
    event.widget.config(bg=arr_col[int(random() * 5)])


def leavemouse(event):
    event.widget.config(bg='#d9d9d9')


arr_dt = ['one', 'two', 'three', 'four', 'five']
arr_col = ['#ffff00', '#55ff7f', '#ffaa7f', '#55ffff', '#ff55ff']

lst = Listbox(root,
              font='Tahoma 14',
              width=24,
              height=5,
              selectmode=MULTIPLE
              )

lst.pack(side=TOP)

root.bind('<Enter>', entermouse)
root.bind('<Leave>', leavemouse)

for i in arr_dt:
    lst.insert(END, i)

for j in range(0, 5):
    lst.itemconfig(j, bg=arr_col[j])

lst.itemconfig(0, bg='#ffff70')

btn = Button(root,
             text="Button",
             font="Tahoma 14",
             bg="#ffff7f",
             borderwidth=2,
             pady=5,
             padx=10,
             relief=RIDGE
             )

btn.pack(pady=10, side=BOTTOM)

btn.bind('<Enter>', handlerenter)
btn.bind('<Leave>', handlerleave)
btn.bind('<Button-1>', handlerclk)

root.mainloop()
