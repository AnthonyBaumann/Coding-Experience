# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:39:24 2022

@author: acbaum1
"""

user_input=input("Provide a list of numbers:")
numList=list(map(int,user_input.split()))

numList.sort()
numList.reverse()
    
    
for num in numList:
    if num%2==0:
        print(f"{num}: Even")
    else: 
        print(f"{num}: Odd")