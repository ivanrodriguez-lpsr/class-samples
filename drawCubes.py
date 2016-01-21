# Simple, it imports the good stuff I mean the packages we will need.
import turtle

# We make a function to make a square that we will need for the cube that we will have but we have to make it piece by piece, colors it with fillcolor option

def drawRightSquare(myTurtle):
  myTurtle.fillcolor("cyan")
  myTurtle.begin_fill()
  myTurtle.left(90)
  myTurtle.forward(20)
  myTurtle.right(60)
  myTurtle.forward(20)
  myTurtle.right(120)
  myTurtle.forward(20)
  myTurtle.right(60)
  myTurtle.forward(20)
  myTurtle.end_fill()

# Makes a funcion to make left side of the cube, uses the fill color to fill it with that color

def drawLeftSquare(myTurtle):
    myTurtle.fillcolor("gold")
    myTurtle.begin_fill()
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.right(120)
    myTurtle.forward(20)
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.end_fill()
    
# makes top square function so that we can later use it on for the cubes, is filled with colors

def drawTopSquare(myTurtle):
  myTurtle.fillcolor("silver")
  myTurtle.begin_fill()
  myTurtle.left(30)
  myTurtle.forward(20)
  myTurtle.left(120)
  myTurtle.forward(20)
  myTurtle.left(60)
  myTurtle.forward(20)
  myTurtle.left(120)
  myTurtle.forward(20)
  myTurtle.end_fill()

#The function that will call all the three square functions so that they can create the perfect square it's not a loop and it also has to go back into position for the top square NOTE TO SELF NEXT TIME MAKE IT LEFT,TOP,RIGHt or RIGHT,TOP,Left SO THAT IT CSNT BE LESS CODE

def makeCube(myTurtle):
  drawRightSquare(myTurtle)
  drawLeftSquare(myTurtle)
  myTurtle.backward(20)
  myTurtle.right(270)
  drawTopSquare(Shawn)

# It's a pain but we have to go on to the next space for the cube so that is what this function does, it goes the right ammount forward so that the cubes can perfectly allign once they are drawn

def makeNextCubesSpace(myTurtle):
    makeCube(myTurtle)
    myTurtle.penup()
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.left(120)
    myTurtle.forward(20)
    myTurtle.right(60)
    myTurtle.forward(20)
    myTurtle.left(30)
    myTurtle.pendown()
    
# This simple block will define a function that will call out another function and use it in a loop, the loop allows it to go again and again to create the rows of cubes.

def makeRow(MyTurtle):
  count = 0
  while count < 5:
    makeNextCubesSpace(Shawn)
    count = count + 1

#This here creates a function that will go back the whole row that we did and will go on to the next row without marking it, creating a new blank space to help us make our new row.

def getIntoPos(myTurtle):  
  myTurtle.penup()
  myTurtle.backward(175)
  myTurtle.left(90)
  myTurtle.forward(40)
  myTurtle.right(120)
  myTurtle.forward(20)
  myTurtle.left(30)
  myTurtle.pendown()

# shawn is born, our turtle who will do his duty and this gives him extra speed so he becomes SS (Super Shawn).

Shawn = turtle.Turtle()
Shawn.speed(10)

# this function has a while statement that will run two functions a certain ammount of times.

def makeAllRows(Shawn):
  count = 0
  while count < 4:
    makeRow(Shawn)
    getIntoPos(Shawn)
    count = count + 1

# Draws our final functionception a function inside another function inside anoth... okay it ends our code for today.
makeAllRows(Shawn)

#usually the code runs really fast then closes so this allows you to look at the code as long as you want.
turtle.exitonclick()
