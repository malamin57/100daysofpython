from turtle import Turtle 

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.update_scorebaord()

    def update_scorebaord(self):
        self.clear()
        self.write(f"Level: {self.level} ", align="left", font=FONT)

    
    def increase_level(self):
        self.level+=1
        self.update_scorebaord()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME Over", align="center", font=FONT)