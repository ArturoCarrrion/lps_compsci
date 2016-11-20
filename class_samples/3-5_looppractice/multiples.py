print("for what numbers would you like the multiples")
num = float(raw_input())
multiple = 0
product = num * multiple
while product < 1000:
	multiple = multiple + 1
	product = num * multiple

	print(str(multiple) + " times " + str(num) + " equals " + str(product))
