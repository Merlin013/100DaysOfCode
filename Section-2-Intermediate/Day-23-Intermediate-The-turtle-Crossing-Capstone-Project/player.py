from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create a turtle player that starts at the bottom of the screen
# and listen for the "Up" keypress to move the turtle
# north. If you get stuck, check the video walkthrough in Step 3.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            # self.goto(STARTING_POSITION)
            return True
        else:
            return False
