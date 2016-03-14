# This line opens the file that we will be reading
walking_file = open("walking_instructions.txt", "r")

# This line of code will set a variable to the opened file 
lineToPrint = walking_file.readline()

# This line will print the lines inside the file in a loop
while lineToPrint != "":
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()

# closes the file 
walking_file.close()
