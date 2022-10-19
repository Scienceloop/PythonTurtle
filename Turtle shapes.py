from turtle import Turtle
import random

tim = Turtle()


for i in range(3,11):
    n=0

    while n<i:
        tim.forward(100)
        tim.right(360/i)
        n+=1
    i+=1

screen = Screen()
screen.exitonclick()
