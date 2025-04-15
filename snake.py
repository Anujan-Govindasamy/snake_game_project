from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
        self.head=self.snake_pieces[0]

    def create_snake(self):
        for coordinates in POSITIONS:
            self.add_segment(coordinates)


    def add_segment(self,coordinates):
        new_piece = Turtle()
        new_piece.shape("square")
        new_piece.penup()
        new_piece.color("white")
        new_piece.goto(coordinates)
        self.snake_pieces.append(new_piece)

    def extend(self):
        self.add_segment(self.snake_pieces[-1].position())


    def move(self):
        for piece_num in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[piece_num - 1].xcor()
            new_y = self.snake_pieces[piece_num - 1].ycor()
            self.snake_pieces[piece_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)