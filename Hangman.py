import random 
words=['lion','dog','cat','tiger','horse','goat','fish','shark','lizard','snake'
       ,'penguin','peacock','bear','zebra','mouse','rat']


word=words[random.randint(0,len(words))-1]

word=list(word)

attempts=0
disp=[]
for i in range(len(word)):
    disp.append('_')
print(disp)

while attempts!=6 and '_' in disp  :
    guess=input('Guess a letter\n')
    
    if guess in word:
        disp[word.index(guess)]=guess
        print(disp)
        print('Attempt Number is '+str(attempts))
        
    else:
        attempts+=1
        print('Attempt Number is '+str(attempts))
        
        
if attempts==6:
    print('The man is dead.The word was '+str(''.join(word)))
else:
    print('The man is alive!!')
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
        
        