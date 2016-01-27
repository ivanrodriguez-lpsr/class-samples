# the best quote-sharing service

class Quote(object):
	def __init__(self, quote_text, user_posted, location, num_likes):
		self.quote_text = quote_text
		self.user_posted, = user_posted
		self.location = location
		self.num_likes = num_likes


	# adds one to th "like" count
	def like(self):
		self.num_likes = self.num_likes + 1
	# takes one away from the 'like' count
	def unlike(self):
		self.num_likes = self.num_likes - 1

	# prints the full quote
	def show_quote(self):
		print ("U: " +self.user_posted)
		print("L: " +self.location)
		print ("Q: " +self.quote_text)
		print("Likes: " + str(self.num_likes))


# add some quotes
x = Quote("Nothing with shawn.", "kevin_is_kool", "San Francisco", 0)
y = Quote("Ugly begins with u", "Ivan", "Lps", 0)
z = Quote("Get out", "Sergio", "Lps", 0)


#print our quotes
z.show_quote()


#put quotes in a list
my_quotes = []
my_quotes.append(x)
my_quotes.append(y)
my_quotes.append(z)
user_quote = "Hello. How are you?"
speaker = "Adele"
location = "London"
my_quotes.append(Quote( user_quote, speaker, location, 0))

for q in my_quotes:
	q.show_quote()

# call our_quote function for all our Quotes objects
