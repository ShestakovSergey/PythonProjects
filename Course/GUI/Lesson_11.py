from tkinter import *
from window import *

root = Tk()
setwindow(root)

label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="#f9ff85")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="#aaffff")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="#aaaaff")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#ff007f")

label1.pack(side=LEFT)
label2.pack(side=RIGHT, fill=X, expand=True)
label3.pack(side=TOP)
label4.pack(side=BOTTOM)

root.mainloop()