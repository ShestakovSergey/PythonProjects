from tkinter import *
from random import *
from window import *

root = Tk()
setwindow(root)

def gen_numb(event):
    label["text"] = int(random() * 100)

button = Button(root, text="Generate random number", font="Tahoma 20", borderwidth=2, relief="raised")
button.pack(pady=10, padx=5)

label = Label(root, text="100", font="Tahoma 20", bg="#ffeaca")
label.pack(pady=10, padx=5)

button.bind("<Button-1>", gen_numb)


root.mainloop()
