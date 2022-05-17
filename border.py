from turtle import Turtle


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(0.2, 30)
        self.penup()


