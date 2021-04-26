from tkinter import *
from PIL import Image, ImageTk


def clicked():
    exec(open('game.py').read())

def clicked_info():
    exec(open('info.py').read())


window = Tk()
window.title("Space emulation")
window.geometry('900x500')

canvas = Canvas(window,width=900, height=500)
image = ImageTk.PhotoImage(Image.open("Wallpaper.jpg"))

canvas.create_image(0,0,anchor=NW, image=image)
canvas.pack

lbl = Label(window, text="Space emulation", font=("Ariak Bold", 50))
# Font шрифт, число размер.
lbl.place(x = 450, y = 150, anchor=CENTER)
# Местоположение
btn1 = Button(window, text="Запустить программу", fg="black", font=("Ariak Bold", 15), width=20,height=1, command=clicked)
btn2 = Button(window, text="Информация", fg="Black", font=("Ariak Bold", 15), width=20,height=1, command=clicked_info)
btn3 = Button(window, text="Выход", fg="Black", font=("Ariak Bold", 15), width=20,height=1, command=window.destroy)
# Кнопка
btn1.place(x = 450, y = 250, anchor=CENTER)
btn2.place(x = 450, y = 295, anchor=CENTER)
btn3.place(x = 450, y = 340, anchor=CENTER)
# test
window.mainloop()