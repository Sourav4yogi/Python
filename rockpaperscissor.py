import random

print('\t This a Rock Paper Scissor game\n\n')

p=int(input('Enter your choice\n'))
if p==1:
		q='Rock'
elif p==3:
	q='Scissors'
else:
	q='Paper'
	
print('You chose '+q)

def comp():
	global c
	global d
	c=random.randint(1,3)
	if c==1:
		d='Rock'
	elif c==3:
		d='Scissors'
	else:
		d='Paper'
	
	print('Computer chose ' +d)
	
	if c==1 and p==1:
		print('Tie')
	elif c==1 and p==2:
		print('You win')
	elif c==1 and p==3:
		print('You lose')
	elif c==2 and p==1:
		print('You lose')
	elif c==2 and p==2:
		print('Tie')
	elif c==2 and p==3:
		print('You win')
	elif c==3 and p==1:
		print('You win')
	elif c==3 and p==2:
		print('You lose')
	else:
		print('Tie')
		
		
	

comp()
