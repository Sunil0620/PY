from turtle import Turtle

class Pause(Turtle):
    def __init__(self):
        super().__init__()
        self.paused = False
        self.hideturtle()
        self.color("white")
        self.penup()

    def toggle_pause(self):
        if not self.paused:
            self.paused = True
            self.goto(0, 0)
            self.write("PAUSED", align="center", font=("Courier", 36, "bold"))
        else:
            self.paused = False
            self.clear()
