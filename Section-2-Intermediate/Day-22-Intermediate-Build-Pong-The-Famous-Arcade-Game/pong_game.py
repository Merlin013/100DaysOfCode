from turtle import Screen, Turtle

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Arcade Pong Game")
screen.bgcolor("black")
screen.tracer(0)


paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)



screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
