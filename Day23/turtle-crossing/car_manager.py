from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            y_random = random.randint(-250, 250)
            new_car.goto(300, y_random)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
