# author: ivan
# makes the choice = 1
choice = 1
#creates the empty dictionary
myContacts = {}
# this asks the user foran input
while choice != 0:
	print("Hello there! What would you like to do?")
	print("1) To add a new contact.")
	print("2) To search for a contact")
	print("3) Print all contacs")
	print("4) Delete contact")
	print("0) Exit out")
	
	
	choice = int(raw_input())
	#inputs the name and the number to the dictionary
	if choice == 1:
		print("What is the name of your new contact?")
		name = raw_input()
		print("Great. Whats the number of your contact?")
		number = raw_input()
		myContacts[name] = number
	#looks for the name and prints it
	if choice == 2:
		print("Whos number do you want?")
		name = raw_input()
		print("Here we are:")
		print(myContacts[name])

	# prints the contacts
	if choice == 3:
		print(myContacts)

	if choice == 4:
		print("Which one")
		delete = raw_input()
		del phoneBook[delete]
