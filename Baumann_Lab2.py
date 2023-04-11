# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 11:44:20 2023

@author: acbaum1
"""
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'Anthony Baumann'
__contact__ = 'acbaum1@ilstu.edu'
__copyright__ = '(c) Anthony Baumann 2023'
__license__ = 'MIT'
__date__ = '1 JANUARY 2022'
__version__ = '0.1'
__status__ = "initial release"
__url__ = "..."

"""
Name:          	filename.py
Compatibility: 	Python 3.7
Description:	Write a description of your script here.

Requires:	Modules/libraries needed to run the script.

Development:	1) List of things to do, if needed.

Author:         Anthony C Baumann
Organization:	Illinois State University
Contact:        acbaum1@ilstu.edu
"""
#--------------------------------------------------
#I created a variable ex1 with the statement that I wanted to print and I /
# called that variable to print.
ex1=('I like python and I am excited to learn more!')
print(ex1)
 
#the variable names are width and lenght and I set them equal to two values.
width= 20
length= 30

# these lines show the formula for the area of a rectangle that uses the two /
# variables that I created in the previous lines as the input for the equation. 
# The second line prints the area of the rectange after the calculations have/
# been made. 
area= width * length 
print(area)

# I added another variable caled depth and set it equal to 10. 
# Then I used the previous variable/equation for area and used it for this line.
# Then i printed the volume variable. 
depth= 10
volume= area * depth
print(volume)

# I created a variable and set it equal to a phrase that I that made into a /
# string by putting it in quotations. 
string=('This is a string')

#I combined the print command and the len() command to print the length of the/
# string variable that I created.
print(len(string))

# Here I did the print statement as normal then picked the index that would /
# give me just the word 'string'. This was the characters from 10-16.
print(string[10:16])

# Here I am using the operator '==' to see if the two values are equal. 
# Then I printed the variable that contained the operation and it printed false
Boolean=(128 == 256)
print (Boolean)

# I used the 'r' before the filepath string to mae sure that it would not give/
# an error. Then I printed the filepath.

filepath = r'C\User\Anthony\Downloads'
print(filepath)

# I thik the zen of python is very black and white just like pyhton. There is /
# no inbetween it will either work or it won't. If it does not work then we /
# need to go back and make it work or in this sense make it perfect.
import this 














