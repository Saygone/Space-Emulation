import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os



def clicked():
    window.destroy()
    import game


def clicked_info():
    os.system('Information.docx')


window = Tk()
window.title("Space emulation")
window.geometry('900x500')

canvas = tkinter.Canvas(window, height=900, width=900)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=450, y=250, anchor=CENTER)

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
# testtest
window.mainloop()