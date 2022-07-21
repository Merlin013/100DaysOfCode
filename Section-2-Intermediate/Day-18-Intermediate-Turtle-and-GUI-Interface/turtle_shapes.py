from turtle import Turtle, Screen
import random


tim = Turtle()
colorList = ['red', 'orange', 'yellow', 'green', 'blue',
             'purple', 'pink', 'brown', 'gray', 'gold']


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(70)
        tim.right(angle)


for shapes_side_n in range(3, 11):
    tim.color(random.choice(colorList))
    draw_shape(shapes_side_n)



screen = Screen()
screen.exitonclick()