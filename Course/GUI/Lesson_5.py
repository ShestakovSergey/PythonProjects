from tkinter import *
from window import *

root = Tk()
setwindow(root)

text = Text(root, bd=2, font="Tahoma 20", bg="aqua", fg="gray", width=24, height=5, padx=20, pady=20)
text.insert(END, "Hello\n")
text.insert(END, "Hello\n")
text.insert(END, "Hello\n")

print(text.get("1.0", END
               ))

text.pack()

root.mainloop()