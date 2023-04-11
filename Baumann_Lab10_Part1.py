# -*- coding: utf-8 -*-
"""
Created on Thur. April 6 10:16:59 2023

@author: acbaum1
"""
#------------------------------------------------------------------------------
__author__ = 'Anthony Baumann'
__contact__ = 'acbaum1@ilstu.edu'
__copyright__ = '(c) Anthony Baumann 2023'
__license__ = 'MIT'
__date__ = '6 April 2023'
__version__ = '0.1'
__status__ = "initial release"
__url__ = "..."

"""
Name:          	Baumann_Lab3.py
Compatibility: 	Python 3.7
Description:	This script is the work done for Lab 10 Numpy and Distance Calc.

Requires:	NumPy.

Development:	1) Grade the script as its written.

Author:         Anthony C Baumann
Organization:	Illinois State University
Contact:        acbaum1@ilstu.edu
"""
#------------------------------------------------------------------------------

#Ex. 1-------------------------------------------------------------------------

#This fist example imports NumPy as the shortend variable np. Then an array is 
#created by manually entering the desired numbers into the np.array command. 
#finally the array is printed.
print("Ex 1")

import numpy as np
A1 = np.array([[0,1,2,],[3,4,5],[6,7,8]])
print(A1)

#Ex. 2-------------------------------------------------------------------------

#In this example the print statement only prints the values from the second row
#of the matirx becauase that is the only input that is given to the statement.
#print matrix A1: not row 0, print row 1, not row 2. 
print('Ex 2')

print(A1[1])

#Ex. 3-------------------------------------------------------------------------


#In this example a new array is created with a min value of -10, a max value 
#of 10 and a matrix size of 10x10. Using the np.random tool fills the 10x10
#matrix with all random values randing from -10 to 10. Then the variable sort1
#is set equal to the tool np.sort which takes the A2 matrix and sorts all of  
#the matrix columns from low to high. Then the sorted matrix is printed.
print('Ex 3')

A2 = np.random.randint(low=-10, high=10, size=(10,10))
sort1 = np.sort(A2, axis=0)
print(sort1)

#Ex. 4------------------------------------------------------------------------

# This example creates a new 5x5 array with random values ranging from 0-5.
# The array is then squared using the **2 syntax and set to the variable 
#squared1. The squared1 variable is then printed to show the new squared matrix
print('Ex 4')

A3 = np.random.randint(low=0, high=10, size=(5,5))
print(A3)
squared1 = A3 **2
print(squared1)

#Ex. 5------------------------------------------------------------------------

# This example creates a new 1x10 array with random float numbers ranging from
#0-1. Then the max, min, and mean of the array are found using their respective
#functions. Finally, the formatted print statements print out each value with
#a string denoting wich value is which. 
print('Ex 5')

A4 = np.random.rand(1,10)
print(A4)
max1 = A4.max()
min1 = A4.min()
mean1 = A4.mean()
print('This is the max:', max1)
print('This is the min:', min1)
print('This is the mean:', mean1)

#Ex. 6------------------------------------------------------------------------

# This example creates a new 1x36 array with random values ranging from 0-10.
# Then the original array is reshaped into a 6x6 array using the .reshape tool.
# after that a copy of the array must be made using the .copy command. Then 
#finally the copy can be resized into a 2x2 array using the .resize command.

print('Ex 6')

A5 = np.random.randint(low=0, high=10, size=(1,36))
print(A5)

A6 = A5.reshape(6,6)
print(A6)

copy1 = A6.copy()
print(copy1)

copy1.resize(2,2)
print(copy1)

#Ex. 7-----------------------------------------------------------------------

#This example creates a new array usinig the linspace command. This array is a
#1-D array with 10 float smaples ranging from 0-100. Then the 0 in the array is
#changed to a nan value so that the mean can be calculated. Then the mean is 
#calculated using he .nanmean command. Each new array was also printed after 
#each change to the array.

print('Ex 7')

A6= np.linspace(0,100,num=10,endpoint=False).astype(float)
print(A6)

A6[0] = np.nan
print(A6)

mean2 = np.nanmean(A6)
print(mean2)

#Ex. 8-----------------------------------------------------------------------

#This example creates two new arrays one 4x4 array with random numbers ranging
#from 0-10 and one 1x4 array with random numbers ranging from 0-10 as well. 
#These two arrays are then combined into 1 array using the .concatenate command
#this command can combine arrays as either a new row or a new column. To add 
#the 1-D array as a new column it must be transposed which is the .T syntax.

print('Ex 8')

A7= np.random.randint(low=0, high=10, size=(4,4))
print(A7)

A8=np.random.randint(low=0, high=10, size=(1,4))
print(A8)

A9=np.concatenate((A7, A8.T),axis=1)

print(A9)

#Ex. 9-----------------------------------------------------------------------

#This example uses the tile method that repeats an array with a set amount of 
#reps. The first array created is a 2x2 array with [0,1] and [1,0] which makes 
#a small checker board. Then the next array is created using the .tile command
#which then repeates the small array that was just created into a large 8x8.

print('Ex 9')

A10 = np.array([[0,1], [1,0]])
print(A10)
A11 = np.tile(A10, (8,8))
print(A11)


#Ex. 10----------------------------------------------------------------------

#This example creates a new 10x10 array of random float numbers then prints 
#that array. Then a mask is created to find all of the values in the array that
#are less than or equal to 0.5. These values are then changed the nan values in
#the last step and the new array is printed.

print('Ex 10')

A11 = np.random.rand(10,10)
print(A11)

mask1 = (A11 <= 0.5)
A11[mask1] = np.nan
print(A11)

#Part 2----------------------------------------------------------------------


















