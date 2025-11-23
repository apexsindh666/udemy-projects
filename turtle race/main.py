import turtle
from turtle import Turtle,Screen
import random
race=False
s=Screen()
s.setup(500,400)
bet=s.textinput("make your bet","which turtle will win the race?")
c=["red","orange","yellow","green","blue","violet"]
p=[-70,-40,-10,20,50,80]
all_turtles=[]
for i in range(6):
    t=Turtle(shape="turtle")
    t.color(c[i])
    t.penup()
    t.goto(-240,p[i])
    all_turtles.append(t)
if bet:
    race=True
while race:
    for i in all_turtles:
        if i.xcor()>230:
            race=False
            wc=i.pencolor()
            if wc==bet:
                print(f"you have won the race,{wc} is the winner")
            else:
                print(f"you lost the bet,{wc} is the winner")
        d=random.randint(0,10)
        i.forward(d)

s.exitonclick()