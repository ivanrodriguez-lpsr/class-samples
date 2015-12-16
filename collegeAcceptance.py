print("How old are you?")
age = int(input())

print("Whats your GPA?")
GPA = float(input())

#if GPA is over 3.0 and age is 16, accept it

if GPA > 3.0 and age > 16:
	print( "Congrats, you're in!")
else:
	print( "Sorry, guess you have to go to Harvard instead.")
	
