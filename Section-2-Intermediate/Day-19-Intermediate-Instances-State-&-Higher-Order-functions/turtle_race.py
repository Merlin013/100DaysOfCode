from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
# Setting the dimensions of the screen
screen.setup(width=500, height=400)
screen.title("Turtle Race !")
screen.bgcolor("black")
screen.bgpic("finish-line3.png")
# Taking input from user using a popup dialogue box
user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle will win the race? 'VIBGYOR' Enter a color: ")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions = [-120, -80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You have won !! The {winning_color} turtle is the winner.")
                break
            else:
                print(f"You have lost :( The {winning_color} turtle is the winner.")
                break
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
