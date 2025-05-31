''' escaping_the_maze : "Lost in Maze" solution for Reeborg's World. 
def turn_right():    
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''
import random
class Maze:     
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]  
        # Creates a 2D list (height rows x width columns) filled with spaces (' '), representing the maze grid.

        self.start = (0, 0)
        # Sets the starting position of the maze at the top-left corner (row 0, column 0).

        self.end = (width - 1, height - 1)
        # Sets the ending position of the maze at the bottom-right corner (last column, last row).
        self.generate_maze()

    def generate_maze(self):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < 0.3:  # Randomly place walls
                    self.grid[y][x] = '#'
                else:
                    self.grid[y][x] = ' '
        self.grid[self.start[1]][self.start[0]] = 'S'  # Start point
        self.grid[self.end[1]][self.end[0]] = 'E'      # End point

    def display(self):
        for row in self.grid:
            print(''.join(row))

if __name__ == "__main__":
    maze = Maze(10, 5)
    maze.display()
