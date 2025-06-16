# Function as Inputs
import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(15)
def move_backward():
    tim.backward(15)
def turn_left():
    tim.left(15)
def turn_right():
    tim.right(15)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick() 
