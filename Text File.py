import os.path
path = 'exampl.txt'
checkFile = os.path.isfile(path)
print(checkFile)
if checkFile == True:
    infile = open(path, 'r')
    readFile = infile.read()
    print(readFile)
else: 
 print('File does not exist')


#'r'= read it
