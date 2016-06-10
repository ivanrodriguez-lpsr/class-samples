# imports what we need to get
import string

# applyCipher.py
# A program to encrypt/decrypt user text
# using Ceasar's Cipher
#
#Author: rc.rodriguez.ivan [at] leadps.org

#makes a mapping of encoded alphabet to decoded alphabet 
#arguments: key
#returns: dictionary of mapped letters
def createDictionary(key):
	# creates both alphabet we need, upper case and lowercase
	alphabet = string.ascii_lowercase
	UpperAlpha = string.ascii_uppercase
	# creates the dictionary we need
	Dictionary = {}
	# these two loops append all the letters in the alphabets to the dictionary that we will use
	for i in range(0, len(alphabet)):
		Dictionary[UpperAlpha[(i + key) % 26]] = UpperAlpha[i] 	
	for i in range(0, len(alphabet)):
		Dictionary[alphabet[(i + key) % 26]] = alphabet[i]
	# returns the complete dictionary
	# appends the other characters by running a loop
	for i in range(32, 64):
		Dictionary[chr(i)] = chr(i)
	return Dictionary

#gets the encrypted message from the user
#arguments: none
#returns: encoded message
def getMessage():
	# ask the user what they want to have encoded, gets their message, and then returns it
	print("What message do you want to encode?")
	message = raw_input()
	return message	


#for each letter in the message; decodes and records
#arguments: decoded message
#returns: none
def decodeMessage(message, dictionary):
	#Creates a blank variabe so that we can input the word.
	newMessage = ""
	#This loop looks at the letter in the message we received, looks at it from our own dictionary, then it appends it to the blank variable for the secret message
	for l in message:
		newMessage = newMessage + dictionary[l] 
	# returns the secret word
	return newMessage
#outputs the decoded message to the terminal
#arguments: decoded message
#returns: none
def printMessage(message):
	# prints the message
	print(message)

#  execution starts here

# ask for the key and message

# this try wll allow the whole code to run and if it cannot run the code it will return an error message
try:
	print("What key would you like to use to decode?")
	key = int(raw_input())

	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Okay, here is your secret message.")
	printMessage(decodedMessage)

# returns the message if there is an error in the encoding or if it's not possible
except: 
	print("Sorry this could not be done.")
