import random

for rolls in range (20):
    randomDice = random.randrange(20)+1
    print(randomDice)
    if randomDice==20:
        print ('Critical Hit')
print ('Done Rolling')

