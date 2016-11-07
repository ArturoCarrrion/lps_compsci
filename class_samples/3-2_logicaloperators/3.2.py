print('what is the amount of your purchase')
purchase = int(raw_input())

print('what is the discunt')
discount = float(raw_input())

if purchase > 1000 and discount == .10:
	print("you spent over $10! your final price is")
	print float(purchase - discount * purchase)


