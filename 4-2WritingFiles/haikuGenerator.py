# Greets the user
print("Hello and welcome to haiku generator")

# Here the users will start to input the lines for the haiku that they will write
print("Provide the first line of your haiku") 
firstLine = raw_input() 
print("Provide the second line of your haiku:") 
secondLine = raw_input()
print("Provide the third line of your haiku:")
thirdLine = raw_input()
print("What would you like to name your file? Dont forget about putting .txt at the end  I took care of it ")
myFile = raw_input() + ".txt"

# opens the file that we will input the lines of the haiku for
TheFile = open(myFile, "w")

# adds the lines of the haikus into the new file
TheFile.write(firstLine + " \n")
TheFile.write(secondLine + " \n") 
TheFile.write(thirdLine + " \n")
# Closed the file for the end of the day
TheFile.close()
