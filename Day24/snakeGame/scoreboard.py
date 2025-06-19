from turtle import Turtle
import os
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    """A class to represent the scoreboard in the snake game."""
    def __init__(self):
        """Initialize the scoreboard with a starting score of 0."""
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        if not os.path.exists("data.txt"):
            with open("data.txt", "w") as file:
                file.write("0")
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        """Reset the score to 0 and update the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     """Display a game over message."""
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    #     # self.hideturtle()
    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()
        