#this a dice simulator

import random

def roll():
	num=random.randint(1,6)
	
	print('The number on the dice is '+ str(num))

while True:
	choice=input('If you wish to roll a dice enter y or enter n  to exit\n')
	if choice=='n':
		exit()
	else:
		roll()






	
	

	