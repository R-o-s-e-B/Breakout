from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3

    def update_score(self):
        self.goto(-300, 300)
        self.write("Score:", align="center", font=("Roboto", 16, "normal"))
        self.goto(-200, 300)
        self.write(self.score, align="center", font=("Roboto", 16, "normal"))
        self.goto(100, 300)
        self.write("Lives:", align="center", font=("Roboto", 16, "normal"))
        self.goto(200, 300)
        self.write(self.lives, align="center", font=("Roboto", 16, "normal"))

    def score_points(self):
        self.clear()
        self.score += 100

    def lose_life(self):
        self.clear()
        self.lives -= 1

    def game_over(self):
        self.clear()
        self.goto(0, 50)
        self.write("Game over", align="center", font=("Roboto", 40, "normal"))
        self.goto(0, 10)
        self.write(f"Score:{self.score}", align="center", font=("Roboto", 20, "normal"))
        self.goto(0, -70)
        self.write("Restarting in 3..2..1..", align="center", font=("Roboto", 20, "normal"))

    def level_two(self):
        self.goto(0, 50)
        self.write("Level One complete", align="center", font=("Roboto", 40, "normal"))
        self.goto(0, 10)
        self.write(f"Score:{self.score}", align="center", font=("Roboto", 20, "normal"))
        self.goto(0, -70)
        self.write("Level two starting in 3..2..1..", align="center", font=("Roboto", 20, "normal"))

    def level_three(self):
        self.goto(0, 50)
        self.write("Level Two complete", align="center", font=("Roboto", 40, "normal"))
        self.goto(0, 10)
        self.write(f"Score:{self.score}", align="center", font=("Roboto", 20, "normal"))
        self.goto(0, -70)
        self.write("Level three starting in 3..2..1..", align="center", font=("Roboto", 20, "normal"))

    def level_won(self):
        self.goto(0, 50)
        self.write("Level Three complete", align="center", font=("Roboto", 40, "normal"))
        self.goto(0, 10)
        self.write(f"Score:{self.score}", align="center", font=("Roboto", 20, "normal"))
        self.goto(0, -70)
        self.write("You won", align="center", font=("Roboto", 20, "normal"))
