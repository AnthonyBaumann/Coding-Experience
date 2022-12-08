# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:31:44 2022

@author: acbaum1
"""

low=int(input("Enter lower threshold:"))
high=int(input("Enter upper threshold:"))
num=int(input("Please enter your non-negative or negative number:"))

numList=[]

while num >= 0:
    numList.append(num) 
    num=int(input("Please enter your non-negative or negative number:"))
    
print(f'The numbers between the lower and upper bpoundaries of {low},{high} that are multiples of 3 are:')

for num in numList:
    if num >= low and num<=high  and num%3==0:
        print(num)
        
