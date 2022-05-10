def setwindow(root):
    root.title("Окно приложения")
    root.resizable(False, False)

    w = 640
    h = 480
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    print(ws, wh)

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))