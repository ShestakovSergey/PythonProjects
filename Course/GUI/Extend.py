from tkinter import *
from window import *

root = Tk()
setwindow(root)

button = Button(root, text='Hello', background='#555', foreground='#ccc', padx='20', pady='8', font='16')
button.pack(pady=5)

b1 = Button(root, text='FLAT', relief=FLAT, padx='20', pady='8', font='16', borderwidth=5)
b2 = Button(root, text='RAISED', relief=RAISED, padx='20', pady='8', font='16', borderwidth=5)
b3 = Button(root, text='SUNKEN', relief=SUNKEN, padx='20', pady='8', font='16', borderwidth=5)
b4 = Button(root, text='GROOVE', relief=GROOVE, padx='20', pady='8', font='16', borderwidth=5)
b5 = Button(root, text='RIDGE', relief=RIDGE, padx='20', pady='8', font='16', borderwidth=5)

b1.pack(pady=5)
b2.pack(pady=5)
b3.pack(pady=5)
b4.pack(pady=5)
b5.pack(pady=5)

root.mainloop()
