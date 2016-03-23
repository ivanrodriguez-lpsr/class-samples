#takes num, an integer
# returns true if num is prime
#returns false if num is composite
def isPrime(num):
	for n in range(2,num):
		if num % n == 0:
			return False
	return True


# Creates an empty list so that it can print the numbers all at once that are prime
primeList = []
# this is a for loop that will go through therange of numbers and will see if they are prime or not, if they are this will add them to the list of primes.
for n in range(2,10000):
	x = isPrime(n)
	if x == True:
		primeList.append(n)
# This opens a file
myFile = open("PrimeList", "w")
#  this writes to the file
myFile.write(str(primeList) + "\n")
# This closes the file
myFile.close()
# prints the numbers
print(primeList)

