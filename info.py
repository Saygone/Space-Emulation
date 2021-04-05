from tkinter import *

window = Tk()
window.title("Space emulation information")
window.geometry('800x600')

def clicked():
    exec(open('game.py').read())

lbl = Label(window, text="Space emulation guide", font=("Ariak Bold", 30))
# Font шрифт, число размер.
lbl.place(x = 400, y = 50, anchor=CENTER)

lbl = Label(window, text="Добро пожаловать в мою программу", font=("Ariak Bold", 20))
lbl.place(x = 400, y = 200, anchor=CENTER)




