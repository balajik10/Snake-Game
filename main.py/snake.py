from turtle import Turtle

# Initialize the snake's segments
S_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20

# Create the snake segments
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head=self.snake_segments[0]

    def create_snake(self):
        for position in S_POSITION:
            self.add_seg(position)

    def add_seg(self,position):
        seg_1 = Turtle('square')
        seg_1.color('white')
        seg_1.penup()
        seg_1.goto(position)
        self.snake_segments.append(seg_1)

    def extend(self):
        self.add_seg(self.snake_segments[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DIS)

    def reset(self):
        for snake in self.snake_segments:
            snake.goto(1000,1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head=self.snake_segments[0]

    def up(self):
        if self.head.heading() != 270:  # Avoid moving into opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


