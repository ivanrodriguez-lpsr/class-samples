# These line of codes will introduce the code and will ask the user for an input
print("Hi welcome to Haiku reader! What will you like to see today? 3 for a haiku for a silly person or 4 for a haiku on writing haikus")
choice = raw_input()

# These two lines will open up the haiku files and then read them
Haiku3 = open("haiku3.txt", "r")
Haiku4 = open("haiku4.txt", "r")

# This block will evaluate the input that was entered and will print either the 3rd or 4th haiku.
if choice == "3":
	print(Haiku3.read())
elif choice == "4":
	print(Haiku4.read())
