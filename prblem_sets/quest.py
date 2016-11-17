print('Welcome to Arturo\'s Quest!')

print('Enter the name of your character:')
charecter_name = raw_input()

print('Enter strength (1-10):')
strength = int(raw_input())

print('Enter health (1-10):')
health = int(raw_input())

print('Enter luck (1-10):')
luck = int(raw_input())

sum = int(luck) + int(strength) + int(health)

if sum <= 15:
	print("your carecter's name is " + charecter_name + " your strength is " + str(strength) + " your health is " + str(health) + " and your luck is " + str(luck))

if sum > 15:
	print('You have give your character too many points! Default values have been assigned, '+ charecter_name)

if sum > 15:
	strength = 5

	health = 5

	luck = 5

	print('strength: ' + str(strength) + ' ,health: ' + str(health) + ' ,luck: ' + str(luck))


print(charecter_name +' , you have come to a fork in the road. Do you want to go right or left?')
print ('Enter right or left!')
direction = str(raw_input())

if direction == "left" and strength >= 4:
	print('you ran into a cliff and need to climb down because its the only way to get to the other side you survive because your strength was high enough you win the game')
if direction == "left" and strength < 4:
	print('you ran in to a cliff and need to climb down because its the only way to get to the other side you did NOT servive because your strenght was not hig enuf you lose the game')

if direction == "right" and health >= 5:
	print('you have come across a river full of deadly fish you were able to servive because your health was ' + str(health) +' you win the game') 
elif direction == "right" and health < 5:
	print('you have come across a river full of deadly fish you were not able to servive because your health was to low, you lose the game')
        
