from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Speed up after each paddle hit

    def detect_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def detect_paddle_collision(self, paddle):
        # Check if ball is near paddle and at correct x position
        if (self.distance(paddle) < 50 and
                abs(self.xcor() - paddle.xcor()) < 20):
            self.bounce_x()

    def is_out_of_bounds(self):
        """Returns 'left' if out left, 'right' if out right, else None."""
        if self.xcor() > 380:
            return "right"
        elif self.xcor() < -380:
            return "left"
        return None

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()
        time.sleep(1)