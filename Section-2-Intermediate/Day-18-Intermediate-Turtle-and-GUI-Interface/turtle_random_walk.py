import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

tim = Turtle()


# colorList = ['red', 'orange', 'yellow', 'green', 'blue',
#             'purple', 'pink', 'brown', 'gray', 'gold']

def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    tup = (r, g, b)
    return tup


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
