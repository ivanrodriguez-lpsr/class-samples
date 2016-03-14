# creates the class and tells the computer what to print if the option is like that
class Player(object):
  def __init__(self, name, age, goals, JerseyNumber, Position):
    self.name = name
    self.age = age
    self.goals = goals
    self.JerseyNumber = JerseyNumber
    self.Position = Position

  def printStats(self):
    print("Name:" + self.name)
    print("Age:" + str(self.age))
    print("Goals:" + str(self.goals))
    print("Jersey Number:" + str(self.JerseyNumber))
    print("Position:" + self.Position) 

def savefile(playerList, filename):
	TheFile = open(filename, "a")
	for informarion in playerList:
		TheFile.write(information.name + " " + str(information.age) + " " + str(information.goals) + " " + str(information.JerseyNumber) + " " + information.Position + "\n")
	TheFile.close()

def loadfile(filename):
	list = []
	file = open((filename), "r")
	ltr = file.readline()
	while ltr != " ":
		myWords = ltr.split()
		print(list)
		list.append(Player(myWords[0], myWords[1], myWords[2], myWords[3], myWords[4]))
		ltr = file.readline()
	TheFile.close()
	return oldPlayers

print("Press 1 to start with a new team, or press 2 to use an old team")
user_choice = raw_input()
if user_choice == "2":
	print("Enter the file name that you had along with .txt at the end")
	filename = raw_input()
	myPlayers = loadfile(filename)
else:
	myPlayers = []

#introduces the code
print("Welcome! Do you wish to add a player to ShawnHigh scoccer team or would you like to view the players?")
print("Enter 1 to add player or enter 2 to view them, 3 to save the file, 0 to get out.")

# creates an option that the user will input
option = raw_input()

# Makes a loop so that the option can print over and over
while option != "0":
  # If the option is 1 then it will ask the player to add the player info
  if option == "1":
    print("Looks like you want to add a player, please enter the information below.")
    print("Name:")
    name = raw_input()
    print("Age in numbers:")
    age = raw_input()
    print("Number of goals they have scored:")
    goals =raw_input()
    print("Please enter the Jersey Number for the player:")
    JerseyNumber = raw_input()
    print("Please enter the position that they play in:")
    Position = raw_input()
    # this here will print a line telling if the user is good or bad depending on the goals they 
    # have made.
    if int(goals) <= 10:
        print ("You suck man, any way.")
    else:
        print("You good fam, any way.")
    
 # will add the new player to the list and then ask the user if they want to change the input 
 # that they had.
	myPlayers.append(Player(name, age, goals, JerseyNumber, Position))
    
	print("Done! Do you want to 1, add another player or do you want 2, to see the players, 3 to save the file. Press 0 to get out")
	option = raw_input()
  
  # If the option that the user inputs is a 2 it will print through this block of code and will 
  # print the whole list that it has then it gives the user another option to change the option.
  elif option == "2":
    print("okay looks like you want to see the players.")
    for information in myPlayers:
        information.printStats()
    print("What do you want to do now? 1 to add another player or 2 to see the players again. Press 0 to get out")
    option = raw_input()
   
  elif option == "3":
	print("Please pick a file name and add '.txt' to the end of the file")
	newfile = raw_input()
	savefile(myPlayers, newfile)
	print("Done, goodbye.")
	option = "0"
