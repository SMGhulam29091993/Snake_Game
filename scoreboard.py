from turtle import Turtle

ALIGNMENT = 'center'

FONT = ('courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    #def game_over(self):
    #    self.goto(0, 0)
    #    self.color('red')
    #    self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
