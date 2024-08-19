from turtle import Turtle
import time



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,278)
        self.hideturtle()
        self.write(("Your Score is: ", self.score), align="center", font=("Arial", 15, "normal"))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        
        self.score = 0
        self.increase_score()


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(("Your Score Is: ",  self.score), align="center",font=("Arial", 15, "normal"))
