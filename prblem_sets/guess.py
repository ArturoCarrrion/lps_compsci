#this block of code is to let the computer decide on a random number to use in the program so the user can guess the number that the computer made up.  
import random 
num = random.randint(1,1000)
#In this block of code it prints out a stament to let the user know to guess the number between 1 and 1000.Also to let the user know to enter there number.
print("Guess my  number Between 1 trough a 1000 !!!")
print('enter your number:')
#the next line sets the verable number to 0.
number = 0
#the next block of code is a while loop that will run if that stament is true wich is if the neumber that the user enters does not equal the same as the number that the computer chose. Also it lets the user enter there number.
while number != num:
	number = int(raw_input())
#the next block is a if stament wich checks if its true or false if the line above does not apply to it so it checks if the number that the user enters is less than the number that the computer chose and lets the user know if the number they enter is to low.  
	if number < num:
		print('to low guess a gain enter your number:')
#the next block is a elif stament wich checks if its true or false so it checks if the number that the user enters is greater than the number that the computer enters it will print the stament to try again.  
        elif number > num:
                print('to hight please enter another number:')
#the next block of code is a else stament wich means that if any of the obove lines of code appply to the users input it will say that they won the game because they guess the corect number. 			
	else:
		print('you won the game!!!')
#the last line is to make the program stop after the user guess the correct number that the computer pick. 
		break
