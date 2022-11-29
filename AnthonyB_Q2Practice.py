# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:42:55 2022

@author: acbaum1
"""

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

my_list=[num1,num2]

if my_list[0]< 10 and my_list[1] < 10:
    print("Both numbers are less than 10")
elif my_list[0] < 10 or my_list[1] < 10:
    print("One of the two numbers is less than 10")
elif my_list[0] >= 10 and my_list[1] >= 10:
    print("Both numbers are two digits")