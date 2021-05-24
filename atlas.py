import tkinter
from tkinter import *
from PIL import Image, ImageTk


def clicked():
    import game


def clicked_info():
    exec(open('info.py').read())


window = Tk()
window.title("Space emulation")
window.geometry('850x650')

canvas = tkinter.Canvas(window, height=650, width=850)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=425, y=325, anchor=CENTER)

# Местоположение
btn1 = Button(window, text="Солнце", fg="black", font=("Ariak Bold", 10), width=10,height=4, command=clicked)
btn2 = Button(window, text="Информация", fg="Black", font=("Ariak Bold", 10), width=10,height=4, command=clicked_info)
btn3 = Button(window, text="Выход", fg="Black", font=("Ariak Bold", 10), width=10,height=4, command=window.destroy)
# Кнопка
btn1.place(x = 125, y = 100, anchor=CENTER)
btn2.place(x = 325, y = 100, anchor=CENTER)
btn3.place(x = 525, y = 100, anchor=CENTER)
# testtest
window.mainloop()