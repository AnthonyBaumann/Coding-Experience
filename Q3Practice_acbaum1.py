# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:32:46 2022

@author: acbaum1
"""

user_int=int(input("Provide a whole number: "))

sum_int=0
int_count=0

while user_int > 0:
    sum_int+=user_int
    int_count+=1
    user_int=int(input("Provide a whole number: "))
else: 
    print('You have entered',(int_count),'numbers that add up to be',(sum_int))