# open a file for writing
# second argument:
# r is for reading 
# r+ is for reading for reading and writing existing file
# w is for writing be carful! starts writing from the beginning.
# a is append * from the end*
myFile = open("numList.txt", "w")

# create a list to write to my file
nums = range(1,1501)

# write each item to the file
for n in nums:
	myFile.write(str(n) + "\n")

# close the file
myFile.close()
