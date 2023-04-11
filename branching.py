import random
#this line imports the random tool which allows my to use a random/
#number generator.

p = random.randint(1, 6)
#This line sets p equal to a random number from 1-6.

if p==6:
    print('You Win!')
#This loop sets the win condition to exactly 6 so if the random number/
#generator gives you a 6 this statement will print.
elif p == 5:
    print("Try again!")
#This loop sets the print condition to exactly 5 so if the random number/
#generator gives you a 5 this statement will print.
else:
    print('You Lose')
#This loop sets the print condition to anyting other than 5 or 6 so if the/
#random number generator gives you anything other than 5 or 6 this statement/
#will print.   
