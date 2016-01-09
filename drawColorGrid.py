import turtle 

def drawRedSquares(myTurtle):
	myTurtle.color("red")
	cnt = 0
	while cnt < 4:
		myTurtle.forward(25)
		myTurtle.right(90)
		cnt = cnt + 1		

def drawBlueSquares(myTurtle):
        myTurtle.color("blue")
        cnt = 0
        while cnt < 4:
                myTurtle.forward(25)
                myTurtle.right(90)
                cnt = cnt + 1

def drawYellowSquares(myTurtle):
        myTurtle.color("yellow")
        cnt = 0
        while cnt < 4:
                myTurtle.forward(25)
                myTurtle.right(90)
                cnt = cnt + 1

def drawGreenSquares(myTurtle):
        myTurtle.color("Green")
        cnt = 0
        while cnt < 4:
                myTurtle.forward(25)
                myTurtle.right(90)
                cnt = cnt + 1


def make4Squares(myTurtle):
	drawGreenSquares(myTurtle)
	myTurtle.left(90)
	drawBlueSquares(myTurtle)
	myTurtle.left(90)
	drawRedSquares(myTurtle)
	myTurtle.left(90)
	drawYellowSquares(myTurtle)
	
def makeAllsquares(myTurtle):
	count = 0
	while count < 5:
		make4Squares(myTurtle)
		myTurtle.left(180)
		myTurtle.penup()
		myTurtle.forward(50)
		myTurtle.left(90)
		myTurtle.forward(25)
		myTurtle.right(180)
		myTurtle.pendown()
		count = count + 1
	








shawn = turtle.Turtle()
makeAllsquares(shawn)
turtle.exitonclick()
