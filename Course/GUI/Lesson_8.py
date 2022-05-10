from tkinter import *
from window import *

root = Tk()
setwindow(root)

text = Text(root, bd=2, font="Tahoma 20", bg="aqua", fg="gray", width=24)
scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)

text.pack()
scrollbar.pack(side=LEFT, fill=Y)

text['yscrollcommand'] = scrollbar.set

root.mainloop()