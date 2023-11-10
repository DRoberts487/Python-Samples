import random
numberRolls=int (input('How many times do you want to roll?'))
numberSides=int (input('How many sides is there?'))
for count in range(numberRolls):
    throw = random.randrange(numberSides)+1
    print ('Roll is:')
    print(throw)
if throw==20:
            print ('Critical Hit')
elif throw==1:
            print ('Critical Miss')





#Make sure your rolls and dice sides are integers
#Ask for the number of rolls
#Ask for the number of sides
#roll the dice
#Output the results to the screen
#Check for a critical hit and output to the screen if it is a critical hit
#Check for a critical miss and output to the screen if it is a critical miss
