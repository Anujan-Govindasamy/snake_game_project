from turtle import Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0,280)
        self.color("white")
        self.write(arg=f"score : {self.score} ",align="center",font=("Courier",15,"normal"))
        self.hideturtle()


    def game_over(self):
        self.goto(x=-70,y=0)
        self.write(arg="game over",font=("Courier",20,"normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"score : {self.score} ",align="center",font=("Courier",15,"normal"))




