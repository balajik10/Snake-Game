from turtle import Turtle
from snake import Snake
FONT=("Courier", 24, "normal")
ALIGNMENT="center"
class GameOver(Turtle,Snake):
    def __init__(self):
        super().__init__()
        # self.score = 0
        self.penup()
        self.color("white")
        # self.goto(0, 260)
        self.hideturtle()

    def game_over1(self):
        self.clear()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    # def reset_snake(self):
    #     for segment in self.snake_segments:
    #         segment.hideturtle()  # Hide each snake segment
    #     self.snake_segments.clear()

