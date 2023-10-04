import random

for rolls in range (20):
    randomDice = random.randrange(20)+1
    print(randomDice)
    if randomDice==20:
        print ('Critical Hit')
    if randomDice==1:
        print ('YOU LOSE,NICE TRY')
    if randomDice==7:
        print ('Roll Again')
    if randomDice==1+1:
        print ('Hello')
    if randomDice==4*4:
        print ('Roll 3 Times')
print ('Done Rolling')

