from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(5, 1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    """Move the paddle up by 20 units."""
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
def go_down():
    """Move the paddle down by 20 units."""
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick() 
