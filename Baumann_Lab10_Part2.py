# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 11:34:24 2023

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
Description:	This script is the work done for Lab 10 part 2. Calculating the
distnace between two points on Earth using the Haversine Formula
Requires:	NumPy.

Development:	1) Grade the script as its written.

Author:         Anthony C Baumann
Organization:	Illinois State University
Contact:        acbaum1@ilstu.edu
"""
#-----------------------------------------------------------------------------
# Here I am importing the libraries that are needed to calculate the Euclidian
#distance.

import math
import sys

#------------------------------------------------------------------------------
    
# This line is the first line that prints and tells the user what this script 
# is and what it will be doing.

print("""
      
Haversine Distance Calculator

Enter the coordinate data points from any two points on Earth 
and enter them when prompted. Then the program will 
calculate the Haversine Distance between them.

""")
#-----------------------------------------------------------------------------
# These lines are now promting the user to input the coordinates of the first
# and second locations. These values are then stored as the variables x1,y1,x2,
# and y2 to be used in the formula later in the script. Then the inputs are 
#converted from a string to a float.

x1 = input('Enter the X coordinate for the first location in deciaml degrees: ' )
y1 = input('Enter the Y coordinate for the first location in deciaml degrees: ' )
x2 = input('Enter the X coordinate for the second location in deciaml degrees: ' )
y2 = input('Enter the Y coordinate for the second location in deciaml degrees: ' )

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
#-----------------------------------------------------------------------------
#These lines of code check the user inputted values to make sure that the user
#entered a number and not a string. The code runs the check for the given
#variable and if it passes then nothing happens and the next check occurs.
#However, if the variable does not pass then an error message pops up telling
#the user which variable was entered wrong and ends the program.


try:
    check_x1 = float(x1)
except ValueError:
    print("You entered something other than a number for x1")
    sys.exit()
try:
    check_y1 = float(y1)
except ValueError:
    print("You entered something other than a number for y1")
    sys.exit()
try:
    check_x2 = float(x2)
except ValueError:
    print("You entered something other than a number for x2")
    sys.exit()
try:
    check_y2 = float(y2)
except ValueError:
    print("You entered something other than a number for y2")
    sys.exit()
#------------------------------------------------------------------------------
#These lines set the minimum at 0 and the absoulte value max for both lat and 
#long. Then using these values the program checks if the user entered values 
# are within these constraints. if they are then the program continues as 
# normal but if they dont fall witin the range then an error messeage is shown.
    
min = 0
maxy = abs(90)
maxx = abs(180)

if (float(x1) <= min and float(x1) >= maxx):
    print('invalid value')
    sys.exit()
elif (float(y1) <= min and float(y1) >= maxy):
    print('invalid value')
    sys.exit()
elif (float(x2) <= min and float(x2) >= maxx):
    print('invalid value')  
    sys.exit()
elif (float(y2) <= min and float(y2) >= maxy):
    print('invalid value')
    sys.exit()
#------------------------------------------------------------------------------
# Here the coordinate values entered by the user are converted to radians to 
#be used in the Haversine formula. Then the delta phi and delta lambda variables
#are created by subtracting the lat and long of each coordinate value entered. 


x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)

dlat = y2_rad - y1_rad
dlong = x2_rad - x1_rad
#------------------------------------------------------------------------------
#These lines are the formulas for the main Haversine formula. Variable a is set
#as the given formula including the detla phi and lambda. Then the variable c
# is set to the given formula and uses variable a. Then variabel R is set to 
#the Earth's mean radius in meters.

a = math.sin(dlat/2)**2 + math.cos(y1_rad) * math.cos(y2_rad) * math.sin(dlong/2)**2

c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

R= 6371008.8
#-----------------------------------------------------------------------------
#These lines re print the enetered coordinates from earlier.

print ('Coordinates entered for location 1:',(x1,y1))
print('Coordinates entered for location 2:',(x2,y2))
#------------------------------------------------------------------------------
#These last few lines calculate the distance using the d=R*c formula and the 
#solution is given in meters. Then the distance is also calculted in kilometers
#and Miles. Finally, the distance is printed in kilometers and miles with no 
#decimals.

print("Calculating distance . . .")

d = R * c
d2=d/1000
d3=d/1609.34

print("The distance in kilometers is %0.0f"%(d2))
print("The distance in miles is %0.0f"%(d3))

print('Finished')














