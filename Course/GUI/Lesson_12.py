from tkinter import *
from window import *

root = Tk()
setwindow(root)


label1 = Label(root, text="Метка 1", font="Tahoma 20", bg="#f9ff85")
label2 = Label(root, text="Метка 2", font="Tahoma 20", bg="#aaffff")
label3 = Label(root, text="Метка 3", font="Tahoma 20", bg="#aaaaff")
label4 = Label(root, text="Метка 4", font="Tahoma 20", bg="#ff007f")

label1.place(x=10, y=0)
label2.place(relx=0.5, rely=0.5, anchor="center")
label3.place(relx=0.5, y=0, anchor="n")

root.mainloop()