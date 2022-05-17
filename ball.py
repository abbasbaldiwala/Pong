
from turtle import Turtle
import random
MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(0.75, 0.75)
        self.has_scored = False

    def reset_ball_l(self):
        self.home()
        heading_right = random.randint(-45, 45)
        self.seth(heading_right)

    def reset_ball_r(self):
        self.home()
        heading_right = random.randint(135, 225)
        self.seth(heading_right)

    def bounce(self):
        if self.heading() < 180:
            new_heading = 180 - self.heading()
            self.seth(new_heading)
        else:
            new_heading = 180 - (self.heading() - 360)
            self.seth(new_heading)

    def border_bounce(self):
        if 90 < self.heading() < 180:
            new_heading = (90 - (self.heading() % 90)) + 180
            self.seth(new_heading)

        elif self.heading() < 90:
            new_heading = -self.heading()
            self.seth(new_heading)

        elif 180 < self.heading() < 270:
            new_heading = 180 - (self.heading() % 90)
            self.seth(new_heading)

        elif self.heading() > 270:
            new_heading = (90 - (self.heading() % 90))
            self.seth(new_heading)

    def move(self):
        self.forward(MOVE_DISTANCE)

