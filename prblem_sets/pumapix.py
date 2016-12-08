# In this block of code it prints out two staments one that welcomes the user and the other lets the user know that they should enter there shows.
print('welcome to pumapix')
print('enter 5 of your favorite tv. shows:')
# In this block of code sets a veriable tv. to 0 and a variable called my_list set to a list that the user will create.Also it prints out a stment to let the user know they should enter the name of the show.The line below that lets the veriable tv_shows to equal what the user inputs.
my_list = []
tv = 0
# then the veriable TV add one vry time the loop runs. Also it runs this loop 5 times because onece the number of tv is higher than 5 it stops runing. 
#then the last line lets the verible tv_shows get put in in to the list from the input that the user put in.  
while tv < 5:
	print('enter a name of a show:')
	tv_shows = str(raw_input())
	tv = tv + 1
	my_list.append(tv_shows)

#this block lets the user know that this is what he put in and then it prints back a list with the users input.  
print('here is what you enter:')
print(my_list)
#the next block has a veriable called add_shows and is set to a list with 2 items. then the next line then makes the list beable to add the other list together to be able to put them together. 
# then the second to last line put the names of the shows in alphabetical order. and the last line set the veriable num to 0.
add_shows = ['csi' , 'family guy']
my_list = my_list + add_shows
my_list.sort()
num = 0 
# This block in the first line lets the user know that this is there list and two more were added. 
# Also the for is a loop that runs in the list to beable to list them out.Also the veriable num is set to be able to add one evry time it list a show.
# The last line lets the list be printed in a individual line and also lets each show that is listed be able to be numberd as well. 
print('here is a list of your shows with two more:')
for things in my_list:
	num = num + 1
	print (str(num) + "." + things)


