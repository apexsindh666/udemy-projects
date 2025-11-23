from turtle import Turtle
START=[(0,0),(-20,0),(-40,0)]
M=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment=[]
        self.create()
        self.head = self.segment[0]

    def create(self):
        for i in START:
            self.add_segment(i)
    def add_segment(self,position):
        s = Turtle("circle")
        s.color("orange")
        s.penup()
        s.goto(position)
        self.segment.append(s)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            self.segment[i].goto(self.segment[i - 1].xcor(), self.segment[i - 1].ycor())
        self.head.forward(M)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)