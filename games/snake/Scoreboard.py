from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        with open("High_Score.txt", "r") as file:
            contents = file.read()
            if contents.strip():
                self.high_score = int(contents)
            else:
                self.high_score = 0

        self.score = 0
        #self.high_score = high_score
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(-20,315)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_Score.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()