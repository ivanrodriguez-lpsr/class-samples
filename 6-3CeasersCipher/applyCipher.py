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
	alphabet = string.ascii_lowercase
	UpperAlpha = string.ascii_uppercase
	print(UpperAlpha)
	Dictionary = {}
        count = 0
	for i in range(0, len(alphabet)):
		Dictionary[UpperAlpha[(i + key) % 26]] = UpperAlpha[i] 	
	for i in range(0, len(alphabet)):
		Dictionary[alphabet[(i + key) % 26]] = alphabet[i]
	Dictionary[" "] = " "
	return Dictionary

#gets the encrypted message from the user
#arguments: none
#returns: encoded message
def getMessage():
	print("What message do you want to encode?")
	message = raw_input()
	return message	


#for each letter in the message; decodes and records
#arguments: decoded message
#returns: none
def decodeMessage(message, dictionary):
	newMessage = ""
	for l in message:
		newMessage = newMessage + dictionary[l] 
		
	return newMessage
#outputs the decoded message to the terminal
#arguments: decoded message
#returns: none
def printMessage(message):
	print(message)

#  execution starts here

# ask for the key and message
try:
	print("What key would you like to use to decode?")
	key = int(raw_input())

	dictionary = createDictionary(key)
	encodedMessage = getMessage()
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Okay, here is your secret message.")
	printMessage(decodedMessage)
except: 
	print("Sorry this could not be done.")
