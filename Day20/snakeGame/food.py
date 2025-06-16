from turtle import Turtle
import random

class Food(Turtle):
    """A class to represent the food in the snake game."""
    def __init__(self):
        """Initialize the food at a random position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random position within the game area."""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        