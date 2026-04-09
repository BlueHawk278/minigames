from turtle import Turtle

class Padel1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)

class Padel2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(-350, 0)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)