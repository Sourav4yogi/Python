import random

print('\tGuess the Number from 1 to 10 in 3 attempts')

num=random.randint(1,10)
def guess():
	global g
	g=int(input('Guess the number\n'))
	return g
	
count=[]

g=None
guess()

while True:
	if g==num and len(count)<=3:
		print('You win\n')
		break
	elif g>num:
		count.append(g)
		
		if len(count)<3:
			print('Try lower\n')
			guess()
		else:
			print('You ran out of chances')
			break
	
	else:
		count.append(g)
		if len(count)<3:
			print('Try higher\n')
			guess()
		else:
			print('You ran out of chances')
			break
		
		


