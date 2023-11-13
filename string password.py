#change password to test
password = 'password!'

print (len(password))

passwordLength = len(password)

if passwordLength <=4:
    print ('password too short')
else:
    print ('password is fine')

invaild = '!'
if invaild in password:
    print ('you cant have a !')
else: print ('no !')
