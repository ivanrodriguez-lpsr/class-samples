# creates the class and tells the computer what to print if the option is like that
class Player(object):
  def __init__(self, name, age, goals):
    self.name = name
    self.age = age
    self.goals = goals
  def printStats(self):
    print("Name:" + self.name)
    print("Age:" + self.age)
    print("Goals:" + self.goals)

# creates new list
myPlayers = []

# introduces the code
print("Welcome! Do you wish to add a player to ShawnHigh scoccer team or would you like to view the players? Enter 1 to add player or enter 2 to view them, 0 to get out.")

# creates an option that the user will input
option = input()

# Makes a loop so that the option can print over and over
while option != "0":
 
 # If the option is 1 then it will ask the player to add the player info 
  if option == "1":
    print("Looks like you want to add a player, please enter the information below.")
    print("Name:")
    name = input()
    print("Age in numbers:")
    age = input()
    print("Number of goals they have scored:")
    goals = input()
    
    # this here will print a line telling if the user is good or bad depending on the goals they have made. 
    if int(goals) <= 10:
        print ("You suck man, any way.")
    else:
        print("You good fam, any way.")
    
    # will add the new player to the list and then ask the user if they want to change the input that they had.
    myPlayers.append(Player(name, age, goals))
    print("Done! Do you want to 1, add another player or do you want 2, to see the players? Press 0 to get out")
    option = input()
  
  # If the option that the user inputs is a 2 it will print through this block of code and will print the whole list that it has then it gives the user another option to change the option. 
  elif option == "2":
    print("okay looks like you want to see the players.")
    for information in myPlayers:
        information.printStats()
    print("What do you want to do now? 1 to add another player or 2 to see the players again. Press 0 to get out")
    option = input()
    
