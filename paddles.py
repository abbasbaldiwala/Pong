from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(1, 5)

    def move_down(self):
        self.seth(90)
        self.forward(25)

    def move_up(self):
        self.seth(270)
        self.forward(25)
