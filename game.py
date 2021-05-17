import turtle
from turtle import Turtle, Screen
from tkinter import*

wn = turtle.Screen()
wn.title("Example Window")
wn.setup(1.0, 1.0)



"""Анимация движения планет"""

planets = {
    'mercury': {'diameter': 0.383, 'orbit': 58, 'speed': 7.5, 'color': 'gray'},
    'venus': {'diameter': 0.949, 'orbit': 108, 'speed': 3, 'color': 'yellow'},
    'earth': {'diameter': 1.0, 'orbit': 150, 'speed': 2, 'color': 'blue'},
    'mars': {'diameter': 0.532, 'orbit': 228, 'speed': 1, 'color': 'red'},
    'Jupiter': {'diameter': 3, 'orbit': 280, 'speed': 0.75, 'color': 'orange'},
    'Saturn': {'diameter': 2, 'orbit': 340, 'speed': 0.5, 'color': 'Yellow'},
    'Uranus': {'diameter': 1.0, 'orbit': 390, 'speed': 0.3, 'color': 'blue'},
    'Neptune': {'diameter': 1.0, 'orbit': 440, 'speed': 0.2, 'color': 'violet'},
    'Pluto': {'diameter': 0.2, 'orbit': 480, 'speed': 0.1, 'color': 'grey'},
}

def setup_planets(planets):
    for planet in planets:
        dictionary = planets[planet]
        turtle = Turtle(shape='circle')

        turtle.speed("fastest")  # speed controlled elsewhere, disable here
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