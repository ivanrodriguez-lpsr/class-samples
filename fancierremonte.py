import turtle
from Tkinter import *

def regular_triangle(myTurtle):
        myTurtle.forward(40)
        myTurtle.left(120)
        myTurtle.forward(40)
        myTurtle.left(120)
        myTurtle.forward(40)
        myTurtle.left(120)


# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
backward = Button(frame, text='backward', command=lambda: shawn.backward(50))
triangle = Button(frame, text='triangle', command=lambda: regular_triangle(shawn))



# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
backward.pack(side=LEFT)
triangle.pack(side=LEFT)

frame.pack()

turtle.exitonclick()
