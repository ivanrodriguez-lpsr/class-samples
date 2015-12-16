import turtle

notshawn = turtle.Turtle()

notshawn.speed(1)

count = 0 
while count < 20:
	notshawn.forward(5)
	notshawn.penup()
	notshawn.forward(5)
	notshawn.pendown()
	count = count + 1


# go to lower left of the screen
notshawn.penup()
notshawn.goto(-100, -55)
# when you get there draw me a circle
notshawn.pendown()
notshawn.circle(10)


turtle.exitonclick()

