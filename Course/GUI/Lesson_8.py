from tkinter import *
from window import *

root = Tk()
setwindow(root)

frame = Frame(root)
frame.pack(side=LEFT)

text = Text(frame, bd=2, font="Tahoma 20", bg="aqua", width=40, height=10)
text.pack(side=LEFT)

scrollbar = Scrollbar(frame, command=text.yview, orient=VERTICAL)
scrollbar.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

root.mainloop()
