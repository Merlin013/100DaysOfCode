from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

tim = Turtle()


def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    tup = (r, g, b)
    return tup


tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(2)

screen = Screen()
screen.exitonclick()
