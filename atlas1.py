import tkinter
from tkinter import *
from PIL import Image, ImageTk

def clicked_moon():
    exec(open('info.py').read())

def clicked_earth():
    exec(open('info.py').read())


window = Tk()
window.title("Атлас")
window.geometry('370x200')

canvas = tkinter.Canvas(window, height=900, width=900)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=185, y=100, anchor=CENTER)

# Местоположение
btn1 = Button(window, text="Луна", fg="black", font=("Ariak Bold", 15), width=20,height=1, command=clicked_moon)
btn2 = Button(window, text="Земля", fg="Black", font=("Ariak Bold", 15), width=20,height=1, command=clicked_earth)

# Кнопка
btn1.place(x = 185, y = 100, anchor=CENTER)
btn2.place(x = 185, y = 50, anchor=CENTER)

# testtest
window.mainloop()