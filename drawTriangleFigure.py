import turtle


def makeTriangle(myTurtle):
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.left(120)
	myTurtle.forward(10)
	myTurtle.right(240)

def makeRow(myTurtle):
	count = 0
	while count < 4:
		makeTriangle(myTurtle)
		myTurtle.penup()
		myTurtle.forward(20)
		myTurtle.pendown()
		count = count + 1
	myTurtle.penup()
	myTurtle.backward(80)
	myTurtle.pendown()

def makeThreeRows(myTurtle):

	cnt = 0
	while cnt < 3:
		makeRow(myTurtle)
		myTurtle.left(30)
		cnt = cnt + 1

def makeAllRows(myTurtle):
	makeThreeRows(myTurtle)
	myTurtle.right(260)
	makeThreeRows(myTurtle)	


shawn = turtle.Turtle()
makeAllRows(shawn)


turtle.exitonclick()
