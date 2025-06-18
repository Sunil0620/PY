from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
class Scoreboard(Turtle):
    """A class to represent the scoreboard in the snake game."""
    def __init__(self):
        """Initialize the scoreboard with a starting score of 0."""
        super().__init__()
        self.penup()
        self.goto(0, 260) 
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        """Update the scoreboard display with the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) 
    def game_over(self):
        """Display a game over message."""
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        # self.hideturtle()
    def increase_score(self):
        """Increase the score by 1 and update the scoreboard."""
        self.score += 1
        self.update_scoreboard()
        