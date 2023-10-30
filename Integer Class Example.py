isInteger = False

while isInteger != True:
    userInput = input ('Enter an integer: ')
    try:
        convertInteger = int(userInput)
        print ('This is an integer;' , convertInteger)
        isInteger = True
    except:
        print ('That is not an integer')
        
    
    
