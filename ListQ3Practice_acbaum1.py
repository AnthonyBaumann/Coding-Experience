# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:01:14 2022

@author: acbaum1
"""

num= int(input('Provide a whole number:'))
num_list=[]

while num > 0:
    num_list.append(num)
    num=int(input("provide a whole number: "))

else: 
    print("you have entered",len(num_list),"numbers that add up to be",sum(num_list))