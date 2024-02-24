from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"] 
starting_move_postion = 5
move_increment = 10 

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = starting_move_postion

    def create_cars(self):
        randomw_chance = random.randint(1,6)
        if randomw_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=2, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250,250 )
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(starting_move_postion)

    def level_up(self):
        self.car_speed += move_increment

