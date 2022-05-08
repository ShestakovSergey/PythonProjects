from window import *

root = Tk()
setwindow(root)

entry = Entry(root, font="Tahoma 20", bg="yellow", fg="green", bd=4)
entry.insert(END, "Hello")
entry.insert(END, "ABC")

print(entry.cget('font'))
print(entry['font'])

entry['font'] = "Tahome 40"

entry_home = Entry(root, font="Tahoma 30", bg="blue", fg="black", bd=6)
mystr = input("Enter any string: ")
entry_home.insert(END, mystr)

entry.pack()
entry_home.pack()

root.mainloop()