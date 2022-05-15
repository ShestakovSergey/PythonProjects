from tkinter import *
from window import *

root = Tk()
setwindow(root)

path_image = input("Enter path to image: ")
x_scale = float(input("Enter scale x: "))
y_scale = float(input("Enter scale y: "))

img = PhotoImage(file=path_image)

if x_scale > 1:
    img = img.zoom(int(x_scale), int(y_scale))
elif x_scale < 1:
    img = img.subsample(int(1 / x_scale), int(1 / y_scale))

lbl_img = Label(root, image=img)
lbl_img.pack()

root.mainloop()