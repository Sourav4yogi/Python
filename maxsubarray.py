
user=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
 
 

all_subs=[]
maxinum=0
maxilist=0

for i in user:	
	for j in range(len(user)):
		
		i=0
		if len(user[i:j])!=0:
			all_subs.append(user[i:j])
			hal=all_subs[-1]			
			if sum(hal)>maxinum:
				maxinum=sum(hal)
				maxilist=hal
	user.pop(0)


print(maxilist)













	
	
	
