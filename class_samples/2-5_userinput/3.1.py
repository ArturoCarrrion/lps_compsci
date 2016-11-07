print("welcome to guess my number")
fave = 13
print("Enter your number")
your_number = raw_input()
your_number = int(your_number)

if your_number > fave:
	print("Sorry, you lose. :(")

if your_number <= fave:
	print("Hooray, you won! Good choice.")
