# for every roll of papaer towels, you get a $0.25 rebate
# but if you buy more then ten rolls, you get $0.35 rebate for each one

# but if you are a value club member
 # you get $2 rebate for buying at least one roll.


# find out if they are value club member
print(" Are you a value club member? Respond yes or no.")
club = raw_input()

# find out how many rolls of paper towels the user bought
print("How many rolls of paper towels did you buy?")
rolls = int(raw_input())

# if they are in the club, they get an extra 2$
if club == "yes":
	print("In the club")
	if rolls > 10:
		rebate = rolls * .35 + 2
	else:
		rebate = rolls * .25 + 2

else:
	print("not in the club")
	if rolls > 10:
                rebate = rolls * .35
	else:
                rebate = rolls * .25 


# print rebate
print("Your rebate is " + str(rebate))


