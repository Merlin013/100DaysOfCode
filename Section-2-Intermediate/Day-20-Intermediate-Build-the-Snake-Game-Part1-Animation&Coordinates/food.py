from turtle import Turtle
import random
#import game_sounds

COLOR = ["red", "blue", "green", "white"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLOR))
        random_x = random.randint(-278, 278)
        random_y = random.randint(-278, 278)
        self.goto(random_x, random_y)
        #game_sounds.spawn_sound()
