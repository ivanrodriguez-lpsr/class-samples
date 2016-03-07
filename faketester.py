 #makes our class
class Player(object):
 # make player object which has their name, age, number of goals they have, jersey number, and position
 def __init__(self, name, age, goals, jersey_number, position):
		 self.name = name
		 self.age = age
		 self.goals = goals
		 self.jersey_number = jersey_number
		 self.position = position
	# makes function that prints stats of their players
def printStats(self):
	 print("Name:" + self.name)
	 print("Age:" + self.age)
	 print("Goals:"+ self.goals)
	 print("Jersey Number:" + self.jersey_number)
	 print("Position:" + self.position)
 # make function that saves the team
def saveTeam(myPlayers, filename):
	# let's open the file and write to it
	my_file = open(filename, "a")
	# makes a loop: for players in myPlayers
 	for p in myPlayers:
  # write to the file
		my_file.write(p.name + " " + str(p.age) + " " + str(p.goals) + " " + str(p.jersey_number) + " " + p. position + "\n")
 	# close the file
 	my_file.close()
 
 # make a function to load the team
def loadTeam(filename):
 	# create an empty list
 	empty_list = []
 	# open file to read it
 	my_file = open(filename, "r")
 	# read each line of the file
 	my_line = my_file.readline()
 	# make a loop
 	while my_line != "":
  # split the lines of the file so it becomes a list
  myWords = my_line.split()
  # add to the list
  empty_list.append(Player(str(myWords[0]), str(myWords[1]), str(myWords[2]), str(myWords[3]), str(myWords[4]) + "\n"))
  # ask for the next line of the file and repeat the same things
  my_line = my_file.readline()
 	# close the file
 	my_file.close()
 	# return the list
 	return empty_list
 
 # ask the user what they want to do
 print("Welcome to Team Manager Deluxe!")
 print("Do you want to start with a new team or open an existing team?")
 print("Enter the # of your choice")
 print("(1) Start with a new team")
 print("(2) Open a file for an existing team")
 # allow them to choose
 choice = raw_input()
 
 # if their choice is 2, then we should load the file team
 if choice == "2":
 	# ask what the name of the file is
 	print("What's the filename for your existing team? Enter the whole name, including its .tmd exetension")
 	# allow them to input it
 	filename = raw_input()
 	# load their team
 	myPlayers = loadTeam(filename)
 # else if they choose 1, start with a new team
 else:
 	myPlayers = []
 
 # ask them what they want to do again.
 print("What do you want to do? Enter the # of your choice and press Enter.")
 print("(1) Add a player")
 print("(2) Print all players")
 print("(3) Save your player list to a file")
 print("(0) Leave the program (save first to avoid losing your data!)")
 # allows them to choose
 choice = raw_input()
 
 # makes loop
 while choice != "0":
 	# if choice is 1, allow them to enter new player
 	if choice == "1":
  print("Alright, you want to add a player.")
  # enter their name
  print("Enter name:")
  name = raw_input()
  # enter their age
  print("Enter age:")
  age = raw_input()
  # enter the number of goals they have
  print("Enter goals:")
  goals = raw_input()
  # enter their jersey number
  print("Enter jersey number:")
  jersey_number = raw_input()
  # enter the position they play in
  print("Enter position:")
  position = raw_input()
  # add it to the list
  myPlayers.append(Player(name, age, goals, jersey_number, position))
  print("Player was succesfully added.")
  # ask what they want to do again
  print("What do you want to do? Enter the # of your choice and press Enter.")
  print("(1) Add a player")
  print("(2) Print all players")
  print("(3) Save your player list to a file")
  print("(0) Leave the program (save first to avoid losing your data!)")
  # allow them to enter their choice
  choice = raw_input
 
 	# if choice is 2, then print the stats
 	elif choice == "2":
  print("Alright you want to see the players.")
  # for each player in the list we should print the stats
  for player in myPlayers:
  # prints stats
  player.printStats()
  # ask what they want to do again
  print("What do you want to do? Enter the # of your choice and press Enter.")
  print("(1) Add a player")
  print("(2) Print all players")
  print("(3) Save your player list to a file")
  print("(0) Leave the program (save first to avoid losing your data!)")
  # allow them to choose
  choice = raw_input()
 
  # if choice is, save their players
 	elif choice == "3":
  # ask what they want to name it
  print("What will be the name of your file? Enter the name, including the .tmd extension.")
  filename = raw_input()
  # save their players and file
  saveTeam(myPlayers, filename)
  # aask what they want to do again
  print("Succesfully saved! You know the drill, what do you want to do?")
  choice = raw_input()
 	# if choice is 0, they should exit the program
 	elif choice == "0":
  print("Thanks, now you can get out =)")
 
 
