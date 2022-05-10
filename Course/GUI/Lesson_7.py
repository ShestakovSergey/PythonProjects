from tkinter import *
from window import *

root = Tk()
setwindow(root)

label = Label(root, text="Ваш любимый цвет", font="Tahoma 20")

choice1 = StringVar()
r1 = Radiobutton(root, text="Красный", font="Tahoma 14", variable=choice1, value="red")
r2 = Radiobutton(root, text="Зеленый", font="Tahoma 14", variable=choice1, value="green")
r3 = Radiobutton(root, text="Чёрный", font="Tahoma 14", variable=choice1, value="black")

choice1.set("red")
print(choice1.get())

choice2 = IntVar()
r4 = Radiobutton(root, text="Красный", font="Tahoma 14", variable=choice2, value=1)
r5 = Radiobutton(root, text="Зеленый", font="Tahoma 14", variable=choice2, value=2)
r6 = Radiobutton(root, text="Чёрный", font="Tahoma 14", variable=choice2, value=3)

choice2.set(1)
print(choice2.get())

label.pack()
r1.pack()
r2.pack()
r3.pack()
r4.pack()
r5.pack()
r6.pack()

root.mainloop()