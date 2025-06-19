from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates for better performance

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Collision with food
    if snake.head.distance(food) < 18:
        #print("ahm ahm ahm ")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect Collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()
    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head == segment:
            pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
