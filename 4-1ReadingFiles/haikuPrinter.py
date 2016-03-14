# This line will import a magul
import time
 
# This line will open up the file and read it to but a specific file
myFirstHaiku = open('haiku1.txt', 'r')
#These two lines will then print out a string telling the user the entire code of one haiku
print('Here is the first haiku:') 
print(myFirstHaiku.read())
 # This line will then print a string that will tell the user what it will do
print('I will give you the second haiku line by line.')
# These two lines will ask the user for the amount of seconds it should wait
print('How many seconds should I wait between lines?') 
seconds = int(raw_input())
 # This line will open the next haiku
mySecondHaiku = open('haiku2.txt', 'r')
 # This line will print the code line by line and then it will close
lineToPrint = mySecondHaiku.readline() 
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds)
myFirstHaiku.close()
mySecondHaiku.close()
