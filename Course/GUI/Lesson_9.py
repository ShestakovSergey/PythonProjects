from tkinter import *
from window import *

root = Tk()
setwindow(root)

cities = []

while True:
    city = input("Введите название города: ")
    if city == "0":
        break
    cities.append(city)

frm = Frame(root)
frm.pack()

lst = Listbox(frm, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)
lst.pack(side=LEFT)

scroll = Scrollbar(frm, command=lst.yview, orient=VERTICAL)
scroll.pack(side=RIGHT, fill=Y)

lst.config(yscrollcommand=scroll.set)

for d in cities:
    lst.insert(END, d)

root.mainloop()
