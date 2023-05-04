from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # food=Turtle("circle")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x=random.randint(-290,290)
        random_y=random.randint(-290,290)
        self.goto(random_x,random_y )