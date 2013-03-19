from Tkinter import *

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

b1 = "up"
xold, yold = None, None

def main():
    root = Tk()
    drawing_area = Canvas(root)
    drawing_area.pack()
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    root.mainloop()

