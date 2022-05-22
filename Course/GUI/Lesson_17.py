from tkinter import *
from window import *

root = Tk()
setwindow(root)


def handlerbutton():
    global en1
    global en2
    global result
    try:
        r = str(float(en1.get()) + float(en2.get()))
        result.config(text='Сумма чисел равна: ' + r)
    except ValueError:
        if (not en1.get()) or (not en2.get()):
            result.config(text='Вы ничего не ввели!')
        else:
            result.config(text='Вы ввели не число')


header = Label(root,
               text='Суммирование чисел',
               font='Tahoma 20'
               )
en1 = Entry(root,
            font='Tahoma 20'
            )
en2 = Entry(root,
            font='Tahoma 20'
            )
btn = Button(root,
             text='Сумма',
             font='Tahoma 20',
             command=lambda: handlerbutton()
             )
result = Label(root,
               font='Tahoma 20'
               )

en1.bind('<Return>', handlerbutton)
en2.bind('<Return>', handlerbutton)

header.place(relx=0.5,
             rely=0.01,
             anchor="n"
             )
en1.place(relx=0.5,
          rely=0.1,
          anchor="n"
          )
en2.place(relx=0.5,
          rely=0.2,
          anchor="n"
          )
btn.place(relx=0.5,
          rely=0.3,
          anchor="n"
          )
result.place(relx=0.5,
             rely=0.4,
             anchor="n"
             )
root.mainloop()
