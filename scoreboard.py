from asyncore import write
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 270)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.write_on_board()

    def write_on_board(self):
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.setposition(0, 270)
        self.score += 1
        self.write_on_board()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

