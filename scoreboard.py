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
        with open("highscore.txt") as open_file:
            self.high_score = int(open_file.read())
        self.write_on_board()

    def write_on_board(self):
        self.write(f"Score: {self.score}    High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.setposition(0, 270)
        # self.score += 1
        self.write_on_board()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as edit_file:
                edit_file.write(str(self.high_score))

        self.score = 0
        self.update_score()
