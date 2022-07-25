from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
# Setting the dimensions of the screen
screen.setup(width=500, height=400)

# Taking input from user using a popup dialogue box
user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle will win the race? 'VIBGYOR' Enter a color: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-120, -80, -40, 0, 40, 80, 120]

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)


screen.exitonclick()
