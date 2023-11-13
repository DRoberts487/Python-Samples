import sys
import random

#print scernario to screen
text = open('scenario game intro.txt', 'r')
textFile = text.read()
print (textFile)
#print setting off
text = open('setting off instructions.txt', 'r')
textFile = text.read()
print (textFile)
#print The Encounter onto the screen
text = open('the encounter step.txt', 'r')
textFile = text.read()
print (textFile)

#pick flee or open door
print ('You have two options open the door which is 0 or flee which is 1(game over)')
userInput = int(input('Which option would you like to pick?'))
Option = int(userInput)   
if Option == 0:
    text = open ('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to: (5) search messy table in room, (3) open door 3 or (4) open door 4')
    userInput = int(input('Which option would you like to pick'))
    Option = int(userInput)
elif Option == 1:
    print ('Game Over')
    sys.exit()

#Search messy table
if Option == 5:
    print ('You can only search the table once and you found a +1')
    text = open ('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('You can either open door 3 or 4')
    userInput = int(input('Which door would you like to open?'))
    Option = int(userInput)

#bedroom
if Option == 4:
    text = open ('bedroom door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('you can (8) search the room, (2) go back, (7) atttempt to open chest')
    userInput = int(input('Which option would you like to pick'))
    Option = int(userInput)
#search bedroom
if Option == 8:
    print ('search does nothing (WASTE OF TIME)')
    print ('You can either (2) go back or (7) attmept to open chest')
    userInput= int(input('which option would you like to pick'))
    Option = int(userInput)

#go back
if Option == 2:
    text = open('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to open door (3) or (4)?')
    userInput = int(input('Which door would you pick'))
    Option = int(userInput)

#kitchen
if Option == 4:
    text = open ('bedroom door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('you can (8) search the room, (2) go back, (7) atttempt to open chest')
    userInput = int(input('Which option would you like to pick'))
    Option = int(userInput)


#open chest
if Option == 7:
    print ('You cant open chest')
    print ('would you like to: (8) search the room or (2)go back')
    userInput = int (input('which option would you like to pick'))
    Option =int(userInput)


#Kitchen
if Option == 3:
    print ('You pick the kitchen')
    text = open('kitchen door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to: (1) search the kitchen, (2) go back, (5) go downstairs')


#Search Kitchen
if Option == 1:
    text = open('kitchen door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Search does nothing(WASTE OF TIME) would you like to (2) go back or (5) go downstairs')
    userInput = int(input('Which option would you like to pick?'))
    Option = int(userInput)

#go back
if Option == 2:
    text = open('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to open door (3) or (4)?')
    userInput = int(input('Which door would you pick'))
    Option = int(userInput)

#kitchen
if Option == 3:
    print ('You pick the kitchen')
    text = open('kitchen door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to: (2) go back, (5) go downstairs')
    userInput = int(input('which option would you like to pick'))
    Option = int(userInput)

#go back
if Option == 2:
    text = open('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to open door (3) or (4)?')
    userInput = int(input('Which door would you pick'))
    Option = int(userInput)

#kicthen
if Option == 3:
    print ('You pick the kitchen')
    text = open('kitchen door.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to: (2) go back, (5) go downstairs')
    userInput =int(input('which option would you like to pick'))
    Option = int(userInput)

#go back
if Option == 2:
    text = open('the encounter step.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to open door (3) or (4)?')
    userInput = int(input('Which door would you pick'))
    Option = int(userInput)

#basement
if Option == 5:
    print ('You pick the basement')
    text = open('basement.txt', 'r')
    textFile = text.read()
    print (textFile)
    print ('Would you like to (9) attck Gryla, (10) persaude Gryla, (11)Consider Gryla?')
    userInput = int(input('Which option would you like to pick'))
    Options = int(userInput)
#persuade gryla
if Option == 10:
    text = open('persuade rules.txt','r')
    textFile = text.read()
    print (textFile)
for rolls in range (20):
    randomDice = random.randrange(20)+1
    grylaDice = random.randrange(20)+4
    print ('Your roll is:')
    print (randomDice)
    print ('Gryla roll is:')                
    print (grylaDice)
    if randomDice>grylaDice:
        print('Gryla is gone')
        print('You gained 1/2 experience')
        print('game over')
        sys.exit()
    if randomDice<grylaDice:
        print('Gryla is still here')
        print(' Would you like to (9) attack or (11) Consider')
        userInput (int ('Which option would you like to choose'))
        Option = int (userInput)
#consider gryla
if Option == 11:
    text = open('consider rules.txt','r')
    textFile = text.read()
    print (textFile)
for rolls in range (20):
    randomDice = random.randrange(20)+1
    grylaDice = random.randrange(20)-2
    print ('Your roll is:')
    print (randomDice)
    print ('Gryla roll is:')
    print (grylaDice)
    if randomDice>grylaDice:
        print('You defeated gryla and cured her')
        print('You gained 1/2 experience')
        print('Game Over')
        sys.exit()
    if randomDice<grylaDice:
        print(' You have not defeated Gryla you have to (9) attack or (10) persuade')
        userInput = int('Which option would you like to choose')
        Option = int(userInput)
#persuade gryla
if Option == 10:
    text = open('persuade rules.txt','r')
    textFile = text.read()
    print (textFile)
for rolls in range (20):
    randomDice = random.randrange(20)+1
    grylaDice = random.randrange(20)+4
    print ('Your roll is:')
    print (randomDice)
    print ('Gryla roll is:')                
    print (grylaDice)
    if randomDice>grylaDice:
        print('Gryla is gone')
        print('You gained 1/2 experience')
        print('game over')
        sys.exit()
    if randomDice<grylaDice:
        print('Gryla is still here')
        print(' Would you like to (9) attack or (11) Consider')
        userInput (int ('Which option would you like to choose'))
        Option = int (userInput)
#Attack gryla
if Option == 9:
    text = open('attack rules.txt','r')
    textFile = text.read()
    print (textFile)
for rolls in range (20):
    randomDice = random.randrange(20)+1
    grylaDice = random.randrange(20)-4
    print(randomDice)
    print (grylaDice)
    if randomDice==12:
            print ('You killed Gryla')
    if randomDice==13:
           print ('You killed Gryla')
    if randomDice==14:
           print ('You killed Gryla')
    if randomDice==15:
           print ('You killed Gryla')
    if randomDice==16:
           print ('You killed Gryla')
    if randomDice==17:
           print ('You killed Gryla')
    if randomDice==18:
           print ('You killed Gryla')
    if randomDice==19:
           print ('You killed Gryla')
    if randomDice==20:
           print ('You killed Gryla')
    if grylaDice == 12:
                print ('Gryla hit')
    if grylaDice == 13:
                print ('Gryla hit')
    if grylaDice == 14:
                print ('Gryla hit')
    if grylaDice == 15:
                print ('Gryla hit')
    if grylaDice == 16:
                print ('Gryla hit')
    if grylaDice == 17:
                print ('Gryla hit')
    if grylaDice == 18:
                print ('Gryla hit')
    if grylaDice == 19:
                print ('Gryla hit')
    if grylaDice == 20:
                print ('Gryla hit')
print('you gained 1/2 experience')
print ('Game Over')
sys.exit()

                
    
                    
    
    
