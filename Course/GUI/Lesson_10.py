from tkinter import *
from window import *

root = Tk()
setwindow(root)

root_h = Tk()
setwindow(root_h)

frame = Frame(root, bd=1)
frame.pack()

text = Text(frame, font="Tahoma 20", bg="aqua", width=40, height=10)
text.pack(side=LEFT)

scrollbar = Scrollbar(frame, command=text.yview, orient=VERTICAL)
scrollbar.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scrollbar.set)

frame1 = Frame(root_h)
frame1.pack()
frame2 = Frame(root_h)
frame2.pack()
frame3 = Frame(root_h)
frame3.pack()

label = Label(frame1, text="Важная форма", font="Tahoma 16")
label.pack()

text1 = Text(frame2, font="Tahoma 16", bg="lightblue", width=20, height=3)
text2 = Text(frame2, font="Tahoma 16", bg="lightgreen", width=20, height=3)
text1.pack()
text2.pack()

button1 = Button(frame3, text="Отправить", fg="black", font="Tahoma 16", relief=GROOVE)
button1.pack()

root_h.mainloop()