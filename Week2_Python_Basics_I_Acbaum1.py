# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
__author__ = 'Ryan Lange'
__contact__ = 'rclang3@ilstu.edu'
__copyright__ = '(c) Ryan Lange 2022'
__license__ = 'MIT'
__date__ = '29 April 2022'
__version__ = '0.1'
__status__ = "initial release"
__url__ = "..."

"""
Name:          	Week2_Python_Basics_I.py
Compatibility: 	Python 3.7
Description:	Lecture script for week 2 of Python Scripting for GIS.

Requires:	N/A

Development:	N/A

Author:         Ryan Lange
Organization:	Illinois State University
Contact:        rclang3@ilstu.edu
"""

#------------------------------------------------------------------------------

# Part 1 - Set Up Spyder Settings

#------------------------------------------------------------------------------

# Part 2 - The Zen of Python (Peters 2004)

# Type this into the console for a surprise.

import this

#------------------------------------------------------------------------------

# Part 3 - Print Statements

# When run, this prints your statement in the console.

print("hello world")

#------------------------------------------------------------------------------

# Part 4 - Variables

# Use single letters, readable names, common abbreviations, etc. as variables.
# Some variable names are reserved for Python functions.

# As short as possible to keep your code compact, but still readable.
# Can't start with a number.
# Avoid using spaces.  Use_underscores_instead.
# The programming convention is to avoid UPPERCASE names.

# Creating an "object" in Python called "variable1" that references something.

variable1 = "something"

# NUMBERS

# Integers - Whole numbers with no decimals.

x = 9
y = 3

z = x / y
print(z)

# Float - Floating point numbers with decimals.

a = 3.33
b = 6.0

c = a * b
print(c)

# STRING

# Text - A sequence of characters.

string1 = "This text is a string."

# To add single quotes and apostrophes, the outer quotes must be double "__".
# Double quotes = string representation.
# Single quotes = Used in expressions, queries, etc.

string2 = "Adding 'quotes' or apostrophe's in a string."

# Numbers can also be a string, but they will be seen as text.

string3 = "12"
string4 = "6.66"

# Changing the string numbers to actual numbers.

number_int = int(string3)
number_float = float(string4)

# If you're not sure what data type a variable is, use the Type function.

type(string1)
type(number_int)
type(number_float)

#------------------------------------------------------------------------------

# Part 5 - String Indexing/Slicing

# Extracting parts of a string.

# | P Y T H O N |
# | 0 1 2 3 4 5 |

string5 = "python"

# Printing the "h" in python.
print(string5[3])

# Printing a range of values from the string.
# Have to set the end as 6 or else it will stop at 5 and cut off the "n".
print(string5[0:6])

#------------------------------------------------------------------------------

# Part 6 - Boolean Values

# Expressions using True/False logic.

# TRUE OR FALSE

spherical_earth = True
flat_earth = False

print("The spherical Earth model is", spherical_earth)
print("The flat Earth model is", flat_earth)

# An ellipsoid model of the Earth is obviously more accurate than a sphere.
# If you want to be a jerk about it.

# COMPARISONS

# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# != not equal

23 > 6
23 <= 6
45 != 23

# == compare the values to see if they are equal

packers = 103
bears = 95

packers == bears

# = set two variables as equal

tom_brady = "7 time Super Bowl champion."
lewis_hamilton = "7 time Formula 1 champion."
tom_brady = lewis_hamilton

tom_brady == lewis_hamilton

#------------------------------------------------------------------------------

# Part 7 - File Paths

# Can be stored as a string variable that can be called on in expressions.
# You have to be very specific for file paths to work in Python.

# MAC and LINUX

# Uses "Unix-style" forward slashes.  

filepath1 = '/User/Ryan/Downloads'

# WINDOWS

# Uses back slashes.

# Long story short, this is incompatible with almost everything non-Windows.

# In the 1980s, MS-DOS already used the forward slash character for something.
# So when they added support for folders, they used the back slash instead.
# As a result, we are stuck dealing with this incompatibility decades later.

# A single backslash is an "escape" operator in Python.
# Ex. Explicit line joining.
# Joining multiple physical lines of code into one logical line.
# https://tinyurl.com/5ywa8ca4

# The bottom line is if you use a Windows file path as is, you will get errors.

filepath2 = "C:\Users\Ryan\Downloads"
print(filepath2)

#------------------------------------------------------------------------------

# Part 8 - "Hacking" Solutions to the Windows File Path Problem

# 1. Change the back slashes to forward slashes.

# Python can correctly interpret forward slash file paths for Windows.
# Scripts written this way will be compatible with Mac/Linux.
# Could cause problems when interacting with other Windows programs/libraries.

filepath3 = 'C:/Users/Ryan/Downloads'

# 2. Use double back slashes.

# The first one "escapes" the string and a single is left in the string.
# This "hack" gets around the compatibility issues between Windows and Python.
# Script will work on Windows but won't be compatible with Mac/Linux.

filepath4 = 'C:\\Users\\Ryan\\Downloads'
print(filepath4)

# 3. Denote the Windows file path as being a "raw" string.

# This also "hacks" the compatibility issues between Windows and Python.
# Script will work on Windows but won't be compatible with Mac/Linux.

filepath5 = r'C:\Users\Ryan\Downloads'
print(filepath5)

# The os.path and pathlib libraries can help us deal with files and paths.
# We will get into those next week.

#------------------------------------------------------------------------------

# Part 9 - Copying File Addresses

# There are multiple ways to easily copy a file address.

# WINDOWS

# Shift + Right-click on the file or folder --> Copy as path.
# In the Windows Explorer address bar, right-click --> Copy address as text.

# MAC AND LINUX

# Option + Right-click on the file or folder --> Copy <name> as Pathname.

# IN SPYDER

# Drag and drop a file into the console window to show the address.

#------------------------------------------------------------------------------

# Part 10 - Input and Output File Paths

# INPUTS

# Example input file path that might be used in a tool or expression.
# Uses a direct path to the desired file.

input1 = 'C:/Users/Ryan/Downloads/input_data.csv'

# OUTPUTS

# Example output file paths that might be used in a tool or expression.
# Could either use a direct path that includes the file name or two variables.

output1 = 'C:/Users/Ryan/Downloads/output_data.csv'

# OR

filepath6 = 'C:/Users/Ryan/Downloads/'
filename1 = 'output_data.csv'

output2 = filepath6 + filename1
print(output2)

# A path with no slash at the end means we're pointing at the folder itself.
# Ex. 'C:/Users/Ryan/Downloads'

# A path with a slash at the end means we're pointing inside the folder.
# Ex. 'C:/Users/Ryan/Downloads/'

#------------------------------------------------------------------------------

# Part 11 - Commenting

# What I've been doing this whole time.
# Use the "hashtag" symbol to comment.

# Use comments throughout your scripts to explain what is happening.
# Readability is just as important as things working correctly in this class.

# The convention is to use "block comments" at the beginning of a code block.
# As opposed to in-line comments that break up a code block.

# You can also "comment out" parts of your script to have them not run.

# Docstrings are strings that start and end with triple quotes.
# These are generally used basically as comments at the beginning of a script.
# Can also indicate a new section, function, module, class, method, etc.

'''
This is a docstring.
'''

#------------------------------------------------------------------------------

# Part 12 - Basic Math Operations

# + addition
# - subtraction
# * multiplication
# / division (regular float division)

2 + 2
5 - 3
6 * 6
7 / 2

# ** exponent

9**2

# // floor division (will round down to the nearest integer)
# ex. 7 / 2 = 3 instead of 3.5

7 // 2

# % modulo (finds the remainder from floor division)
# ex. 7 / 2 = 3 with a remainder of 1

7 % 2

# We will cover more operations that require the math module next week.

#------------------------------------------------------------------------------

# Part 13 - Python Formatting Guidelines

# https://peps.python.org/pep-0008/

# There's a lot here, right now we're just worried about one thing.

# The Python convention is to limit lines to a maximum of 79 characters.
# Spyder shows a vertical line to tell you when to stop.  ------------------->

# This makes it easier to have scripts open side by side.
# Ex. Code reviewing tools that show two versions in adjacent columns.
# A little over sometimes is fine, but generally keep it within the limit.

# I will show you how to continue a line of code in part 3.

#------------------------------------------------------------------------------

# References

# Peters, Tim. 2004. The Zen of Python. https://peps.python.org/pep-0020/.

#------------------------------------------------------------------------------