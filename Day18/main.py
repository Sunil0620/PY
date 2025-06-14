import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.pencolor("brown")
# screen.exitonclick()

# for _ in range(4):
#     timmy.forward(200)   # draw square:
#     timmy.left(90)

# for dash in range(15):
#     timmy.forward(10)
#     timmy.penup()          # dash line
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["medium aquamarine", "dark orange", "light coral", "gold", "light blue", "medium violet red",
#           "medium spring green", "plum", "sandy brown", "orchid"]
# timmy.shape("turtle")
# timmy.speed("fastest")
# timmy.pensize(3)
# def draw_shape(num_sides):   # Draw different shapes
#     angel = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angel)
# for shape_side in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)
# screen.exitonclick()

screen.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):       # Draw Spirograph
    for _ in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)
draw_spirograph(5)

screen.exitonclick()
