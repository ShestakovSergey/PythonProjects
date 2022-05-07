from window import *
from random import *

root = Tk()
setwindow(root)

numb = int(random() * 100)

label = Label(root, text=numb)

label.pack()

root.mainloop()