print('Welcome to arturo\'s Quest!')

print('Enter the name of your character:')
charecter_name = raw_input()

print('Enter strength (1-10):')
strength = raw_input()

print('Enter health (1-10):')
health = raw_input()

print('Enter luck (1-10):')
luck = raw_input()

sum = int(luck) + int(strength) + int(health)

if sum <= 15:
	print("your carecter's name is " + charecter_name + " your strength is " + str(strength) + " your health is " + str(health) + " and your luck is " + str(luck))

if sum > 15:
	print('You have give your character too many points! Default values have been assigned, Binky Bop:')

if sum > 15:
	strength = 5

	health = 5

	luck = 5

	print('strength: ' + str(strength) + ' ,health ' + str(health) + ' ,luck: ' + str(health))


print('Binky Bop, you have come to a fork in the road. Do you want to go right or left?')
