import os
import turtle
from tkinter import *
from turtle import Turtle, Screen

wn = turtle.Screen()
wn.title("Solar system")
wn.setup(1.0, 1.0)

turtle.bgcolor("black")

window = Tk()
window.title("Справка")
window.geometry('370x200')


def clicked():
    os.system('atlas.py')


btn1 = Button(window, text="Планеты", fg="black", font=("Ariak Bold", 15), width=20,height=1, command=clicked)
btn1.place(x = 185, y = 100, anchor=CENTER)






"""Анимация движения планет"""

planets = {
    'sun': {'diameter': 4, 'orbit': 0, 'speed': 0, 'color': 'yellow'},
    'mercury': {'diameter': 0.383, 'orbit': 58, 'speed': 4, 'color': 'gray'},
    'venus': {'diameter': 0.949, 'orbit': 108, 'speed': 1.6, 'color': 'yellow'},
    'earth': {'diameter': 1.0, 'orbit': 150, 'speed': 1, 'color': 'blue'},
    'mars': {'diameter': 0.532, 'orbit': 208, 'speed': 0.5, 'color': 'red'},
    'Jupiter': {'diameter': 3, 'orbit': 250, 'speed': 0.1, 'color': 'orange'},
    'Saturn': {'diameter': 2, 'orbit': 310, 'speed': 0.03, 'color': 'Yellow'},
    'Uranus': {'diameter': 1.0, 'orbit': 360, 'speed': 0.01, 'color': 'blue'},
    'Neptune': {'diameter': 1.0, 'orbit': 420, 'speed': 0.006, 'color': 'violet'},
    'Pluto': {'diameter': 0.2, 'orbit': 460, 'speed': 0.004, 'color': 'grey'},
}

def setup_planets(planets):
    for planet in planets:
        dictionary = planets[planet]
        turtle = Turtle(shape='circle')

        turtle.speed("fastest")
        turtle.shapesize(dictionary['diameter'])
        turtle.color(dictionary['color'])
        turtle.pu()
        turtle.sety(-dictionary['orbit'])
        turtle.pd()

        dictionary['turtle'] = turtle

    screen.ontimer(revolve, 50)

def revolve():
    for planet in planets:
        dictionary = planets[planet]
        dictionary['turtle'].circle(dictionary['orbit'], dictionary['speed'])

    screen.ontimer(revolve, 50)

screen = Screen()
setup_planets(planets)
screen.exitonclick()
wn.mainloop()