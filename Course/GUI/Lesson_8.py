from tkinter import *
from window import *

root = Tk()
setwindow(root)

text = Text(root, bd=2, font="Tahoma 20", bg="aqua", width=40, height=10)
text.pack(side=LEFT)

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)
scrollbar.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scrollbar.set)
#text['yscrollcommand'] = scrollbar.set

root.mainloop()