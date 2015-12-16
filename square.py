#square.py

import turtle

# make our turtle
buzz = turtle.Turtle()

# buzz makes a square
lines = 0
while lines < 4:
	buzz.forward(150)
	buzz.left(180)
	lines = lines + 1

turtle.exitonclick()

