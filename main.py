from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("green")
i=0
while i<4:
    timmy.forward(100)
    timmy.left(90)
    i+=1

screen = Screen()
screen.exitonclick()
