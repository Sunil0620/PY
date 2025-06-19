from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    """A class to represent the snake in the game."""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        """Initialize the snake with three segments at starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        """Add a new segment to the snake at the position of the last segment."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    def extend(self):
        """Extend the snake by adding a new segment at the position of the last segment."""
        self.add_segment(self.segments[-1].position())
    def reset(self):
        """Reset the snake to its initial state."""
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def move(self):
        """Move the snake forward by moving each segment to the position of the previous segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        """Change the direction of the snake to up."""
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        """Change the direction of the snake to down."""
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):    
        """Change the direction of the snake to left."""
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        """Change the direction of the snake to right."""
        if self.head.heading() != 180:
            self.head.setheading(0)   
