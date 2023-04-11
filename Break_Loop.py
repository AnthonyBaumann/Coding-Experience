#Name:Anthony Baumann
#Date: 2/9/2023
# Description: This script demonstrates how to break a loop

from math import sqrt
#this line imports the math tool and more specifically the square root tool.
for i in list(range(1000, 0, -1)):
#this line creates a list from 1,000 down to 0 counting down using ',-1'.
    root = sqrt(i)
#this line sets root equal to the square root of the number in the list.
    if root == int(root):
# This line evaluates whether the root variable is equal to a whole number 
        print(i)
        break
# These two lines print the largest number under 1,000 whos square root is a/
#a whole number.
