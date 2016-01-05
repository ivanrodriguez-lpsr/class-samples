import turtle

def drawSide(myTurtle):
	count = 0
	while count < 4:
		drawVee(myTurtle)
		count = count + 1


def drawVee(myTurtle):
	myTurtle.forward(10))
	myTurtle.right(90)
	myTurtle.forward(10)
	myTurtle.left(90)

shawn = turtle.Turtle()
count = 0
while count < 4:
	drawSide(shawn)
	shawn.right(90)
	count = count + 1
turtle.exitonclick()
