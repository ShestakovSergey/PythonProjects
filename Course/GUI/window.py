from tkinter import *
#from tkmacosx import *

def setwindow(root):
    root.title("Окно приложения")
    root.resizable(False, False)

    w = 1000
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    print(ws, wh)

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))
