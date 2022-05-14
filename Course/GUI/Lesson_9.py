from tkinter import *
from window import *

root = Tk()
setwindow(root)

data = ["Apple", "Orange", "Lemon"]

list2 = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)
list2.pack()

for d in data:
    list2.insert(END, d)

list2.selection_set(0, 2)
print(list2.selection_get())

cities = []

while True:
    city = input("Введите название города: ")
    if city == "0":
        break
    cities.append(city)

list1 = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=MULTIPLE)
list1.pack(side=LEFT)

scroll = Scrollbar(root, command=list1.yview, orient=VERTICAL)
scroll.pack(side=LEFT, fill=Y)

list1.config(yscrollcommand=scroll.set)

for d in cities:
    list1.insert(END, d)


root.mainloop()