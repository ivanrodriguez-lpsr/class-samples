import turtle


def drawTee(myTurtle):
	myTurtle.forward(200)
	myTurtle.backward(50)
	myTurtle.right(90)
	myTurtle.forward(50)
	myTurtle.backward(100)
	myTurtle.forward(50)
	myTurtle.right(90)
	myTurtle.forward(150)

def drawFourTee(myTurtle):
	count = 0
	while count < 4:
		drawTee(myTurtle)
		myTurtle.right(90)
		count = count + 1

shawn = turtle.Turtle()

drawFourTee(shawn)
turtle.exitonclick()

# make your turtle down here and pass it to the appropriate places
