#applyCipher.py
#A program to encrypt/decrypt user text
#using Ceasar's Cipher
#
#Author: rc.rodriguez.ivan [at] leadps.org

#makes a mapping of encoded alphabet to decoded alphabet 
#arguments: key
#returns: dictionary of mapped letters
def createDictionary(key):
	#place holder
	return{}
#gets the encrypted message from the user
#arguments: message
#returns: encoded message
def getMessage():
pass


#for each letter in the message; decodes and recods
#arguments: decoded message
#returns: none
def decodeMessage(message, dictionary):
pass

#outputs the decoded message to the terminal
#arguments: decoded message
#returns: none
def printMessage(message):
pass

#  execution starts here

#ask for the key
print("What key would you like to use to decode?")

key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)

printMessage(decodedMessage)
