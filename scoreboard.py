from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_jump_scare = 0
        self.r_jump_scare = 0
        self.high_score = 0  # New attribute for high score
        self.load_high_score()  # Load high score from file
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 180)
        self.write(f"Score: {self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 180)
        self.write(f"Score: {self.r_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(0, 230)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.l_jump_scare = 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.r_jump_scare = 1
        self.update_scoreboard()

        # Update high score if needed
        if self.r_score > self.high_score:
            self.high_score = self.r_score
            self.save_high_score()
