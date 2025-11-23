from turtle import Turtle
A="center"
F=("Arial", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()
    def update(self):
        self.write(f"score: {self.score}", align=A, font=F)
    def game_over(self):
        self.goto(0,0)
        self.write("game over",align=A,font=F)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()
