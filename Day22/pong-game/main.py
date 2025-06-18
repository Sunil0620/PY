from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from pause import Pause
import time

screen = Screen()
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

pause = Pause()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(lambda: globals().__setitem__('game_is_on', False), "q")
screen.onkey(pause.toggle_pause, "p")

game_is_on = True
while game_is_on:
    if pause.paused:
        screen.update()
        time.sleep(0.1)
        continue
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Collision with right paddle (only if moving right)
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 and ball.x_move > 0:
        ball.bounce_x()
        ball.move_speed *= 0.9  # Update speed after every paddle collision

    # Collision with left paddle (only if moving left)
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50 and ball.x_move < 0:
        ball.bounce_x()
        ball.move_speed *= 0.9  # Update speed after every paddle collision
    
    # Detect R Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(0.5)  # Pause after point
        
    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(0.5)  # Pause after point
        
screen.exitonclick()
