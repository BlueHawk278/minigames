from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
from turtle import Turtle
import time


screen = Screen()
screen.setup(width=600, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Creates Border near top of screen
turtle = Turtle()
turtle.goto(-300, 300)
turtle.pendown()
turtle.color("white")
turtle.forward(600)
turtle.penup()
turtle.hideturtle()

screen.listen()

# Allows movement for arrow keys
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

# Allows movement for WASD
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.score += 1
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 300 or snake.head.ycor() < -350:
        snake.kill()
        snake.reset_snake()
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.kill()
            snake.reset_snake()
            scoreboard.reset()

screen.exitonclick()