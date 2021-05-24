import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk

def clicked_sun():
    os.system('sun.docx')

def clicked_mercury():
    os.system('merc.docx')

def clicked_venus():
    os.system('ven.docx')

def clicked_earth():
    os.system('atlas1.py')

def clicked_mars():
    os.system('mars.docx')

def clicked_jupiter():
    os.system('jupiter.docx')

def clicked_saturn():
    os.system('saturn.docx')

def clicked_uranus():
    os.system('uran.docx')

def clicked_neptune():
    os.system('neptun.docx')

def clicked_pluto():
    os.system('pluto.docx')


window = Tk()
window.title("Атлас")
window.geometry('850x650')

canvas = tkinter.Canvas(window, height=650, width=850)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=425, y=325, anchor=CENTER)

# Местоположение
btn1 = Button(window, text="Солнце", fg="black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_sun)
btn2 = Button(window, text="Меркурий", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_mercury)
btn3 = Button(window, text="Венера", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_venus)
btn4 = Button(window, text="Земля", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_earth)
btn5 = Button(window, text="Марс", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_mars)
btn6 = Button(window, text="Юпитер", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_jupiter)
btn7 = Button(window, text="Сатурн", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_saturn)
btn8 = Button(window, text="Уран", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_uranus)
btn9 = Button(window, text="Нептун", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_neptune)
btn10 = Button(window, text="Плутон", fg="Black", font=("Ariak Bold", 10), width=10, height=4, command=clicked_pluto)
btn11 = Button(window, text="Закрыть", fg="Black", font=("Ariak Bold", 10), width=30, height=4, command=window.destroy)
# Кнопка
btn1.place(x=125, y=100, anchor=CENTER)
btn2.place(x=325, y=100, anchor=CENTER)
btn3.place(x=525, y=100, anchor=CENTER)
btn4.place(x=725, y=100, anchor=CENTER)
btn5.place(x=125, y=250, anchor=CENTER)
btn6.place(x=325, y=250, anchor=CENTER)
btn7.place(x=525, y=250, anchor=CENTER)
btn8.place(x=725, y=250, anchor=CENTER)
btn9.place(x=325, y=400, anchor=CENTER)
btn10.place(x=525, y=400, anchor=CENTER)
btn11.place(x=425, y=550, anchor=CENTER)
# testtest
window.mainloop()