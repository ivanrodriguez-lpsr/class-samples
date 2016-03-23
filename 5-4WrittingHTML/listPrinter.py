

#takes num, an integer
# returns true if num is prime
#returns false if num is composite
def isPrime(num):
	for n in range(2,num):
		if num % n == 0:
			return False
	return True

# This line will test if the nuber is true or not			
print("This should be true:")
# Test wha the number is using the function
print(isPrime(11))
# The next two lines will do the same as the previous two
print("This should be false:")
print(isPrime(9))

# Creates an empty list so that it can print the numbers all at once that are prime
primeList = []
# this is a for loop that will go through therange of numbers and will see if they are prime or not, if they are this will add them to the list of primes.
for n in range(2,10000):
	x = isPrime(n)
	if x == True:
		primeList.append(n)
myFile = open("PrimeList", "w")
myFile.write(str(primeList) + "\n")
myFile.close()

