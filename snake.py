from turtle import Turtle

COORDINATE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_increment = 0.1

    def create_snake(self):
        """This function will create 3 snake to give length to it"""
        for i in COORDINATE:
            self.add_segment(i)

    def add_segment(self, i):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(i)
        self.segments.append(new_snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
        self.move_increment *= 0.9

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.move_increment = 0.1

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[position - 1].xcor()
            y_axis = self.segments[position - 1].ycor()
            self.segments[position].goto(x_axis, y_axis)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
