import time

a=[2,11,7,15]

target=9

b=[]


complements={}
			
for i,num in enumerate(a):
	complement=target - num
	
	if complement in complements:
		print(complements[complement])
		print(i)
		b.append(complements[complement])
		b.append(i)
		break 
		
	complements[num]=i
		
		
print(b)

time.sleep(100)
