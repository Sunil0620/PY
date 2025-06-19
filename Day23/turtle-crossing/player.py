from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        self.goto(STARTING_POSITION)
    
    def has_finished(self):
        return self.ycor() > FINISH_LINE_Y
