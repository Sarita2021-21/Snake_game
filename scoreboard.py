from turtle import Turtle
alignment_1="center"
font_1=("courier", 16,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("blue")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",font=font_1,align=alignment_1)
        
        
    def increase_score(self):
       self.score+=1
       self.clear()
       self.update_scoreboard()
    
    
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game over!",font=font_1,align=alignment_1)