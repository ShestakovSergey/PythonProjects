from tkinter import *
from window import *

root = Tk()
setwindow(root)

text = Text(root, bd=2, font="Tahoma 20", bg="aqua", fg="gray")
text.insert(END, "Hello\n")
text.insert(END, "Hello\n")
text.insert(END, "Hello\n")

print(text.get("1.0", END))

text.pack(pady=30, padx=10)

root.mainloop()
