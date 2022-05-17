from turtle import Turtle



FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.pu()
        self.hideturtle()

    def print_scoreboard(self):
        self.write(self.score, False, ALIGNMENT, FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", font=FONT, align=ALIGNMENT)
