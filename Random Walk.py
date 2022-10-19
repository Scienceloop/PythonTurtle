from turtle import Turtle
import random

tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.pensize(10)

for i in range(200):
    tim.pencolor(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.randint(0,360))

screen = Screen()
screen.exitonclick()
