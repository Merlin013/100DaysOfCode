from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import game_sounds

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_sounds.bg_music()

screen.listen()  # to start listening to keystrokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food object
    if snake.head.distance(food) < 15:
        game_sounds.eaten()
        food.refresh()
        # game_sounds.food_spawn()
        snake.extend()

        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_sounds.dead()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_sounds.dead()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
