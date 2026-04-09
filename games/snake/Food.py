from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # When there is a collision with the food, this method moves it to somewhere else
    def refresh(self):
        # pick coordinates snapped to the 20px grid within safe bounds
        possible_x = range(-280, 281, 20)
        possible_y = range(-280, 281, 20)
        random_x = random.choice(possible_x)
        random_y = random.choice(possible_y)
        self.goto(random_x, random_y)