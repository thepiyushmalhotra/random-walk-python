from turtle import *
import random

yertle = Turtle()
yertle.shape("circle")

colours = ["#69FFF1","#2A324B","#EE6352","#F03A47","#E4FF1A", "#BA3B46", "#ED9B40", "#363946", "#139A43", "#FFE2D1"]
directions = [0, 90, 180, 270]

for _ in range(500):
    yertle.color(random.choice(colours))
    yertle.speed(0)
    yertle.pensize(15)
    yertle.forward(30)
    yertle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
