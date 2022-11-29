# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:36:47 2022

@author: acbaum1
"""

num_1= int(input('Input first integer:'))
num_2= int(input('Input second integer:'))

my_list=[num_1,num_2]

if my_list[0]>my_list[1]:
    print('The new number is:',my_list[0]*my_list[0])
    
elif my_list[1]>my_list[0]:
    print('The new number is:',my_list[1]*my_list[1])
    
elif my_list[0]==my_list[1]:
    print('The new number is:'my_list[0]+my_list[1])