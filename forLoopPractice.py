# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:21:02 2022

@author: acbaum1
"""

evenList=[]

for i in range(10):
    num=int(input('Provide a whole number:'))
    if num%2==0:
        evenList.append(num)
        

print('The even numbers in reverse order are:')
for i in range(len(evenList)-1,-1,-1):
    print(evenList[i],end=' ')