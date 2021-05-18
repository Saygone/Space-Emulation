import tkinter
from tkinter import *
from PIL import Image, ImageTk


#def clicked():
    #import game


window = Tk()
window.title("Атлас космических тел")
window.geometry('850x650')

canvas = tkinter.Canvas(window, height=650, width=850)
image = Image.open("Wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.place(x=425, y=325, anchor=CENTER)

# Местоположение
btn1 = Button(window, text="Солнце", fg="black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn2 = Button(window, text="Меркурий", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn3 = Button(window, text="Венера", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn4 = Button(window, text="Земля", fg="black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn5 = Button(window, text="Марс", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn6 = Button(window, text="Юпитер", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn7 = Button(window, text="Сатурн", fg="black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn8 = Button(window, text="Уран", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn9 = Button(window, text="Нептун", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn10 = Button(window, text="Плутон", fg="Black", font=("Ariak Bold", 15), width=150,height=200, command=window.destroy)
btn11 = Button(window, text="Выход", fg="Black", font=("Ariak Bold", 15), width=350,height=100, command=window.destroy)
# Кнопка
btn1.place(x = 125, y = 100, anchor=CENTER)
btn2.place(x = 325, y = 100, anchor=CENTER)
btn3.place(x = 525, y = 100, anchor=CENTER)
btn4.place(x = 725, y = 100, anchor=CENTER)
btn5.place(x = 125, y = 250, anchor=CENTER)
btn6.place(x = 325, y = 250, anchor=CENTER)
btn7.place(x = 525, y = 250, anchor=CENTER)
btn8.place(x = 725, y = 250, anchor=CENTER)
btn9.place(x = 325, y = 400, anchor=CENTER)
btn10.place(x = 550, y = 400, anchor=CENTER)
btn11.place(x = 425, y = 550, anchor=CENTER)
# testtest
window.mainloop()