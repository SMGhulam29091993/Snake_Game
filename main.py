from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(snake.move_increment)

    snake.move()
    # Detecting collission between food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #game_on = False
        scoreboard.reset_score()
        snake.reset_snake()


    # Detect collision with tail
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            #game_on = False
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()

