#find out price from the user
print("What is the price?")
price = int(input())
#calculat the discount price
discount_price = .9 * price
#if the user gets a discount, tell them.
#if not, tell them.
if price > 1000:
	print("Your price is " + str(discount_price))
else:
	print("then the cost is " +  str(price))
