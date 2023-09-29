gpaOne=4
gpaTwo=3
gpaThree=2

creditsOne=6
creditsTwo=5
creditsThree=1

totalCredits = creditsOne+creditsTwo+creditsThree

weightedOne=gpaOne*creditsOne
weightedTwo=gpaTwo*creditsTwo
weightedThree=gpaThree*creditsThree

totalWeighted=weightedOne+weightedTwo+weightedThree

finalGPA=round (totalWeighted/totalCredits,2)

print ('Your Gpa is:',finalGPA)

