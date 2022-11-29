# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:35:46 2022

@author: acbaum1
"""

user_input=input("Create a list of numbers: ")
numberList=list(map(int,user_input.split()))

index=int(input(f"Enter a number between 0,{len(numberList)-1}: "))        
numberList.pop(index) 

print("The modified list is:")
for num in numberList:
    print(num,end = " ")
    

    