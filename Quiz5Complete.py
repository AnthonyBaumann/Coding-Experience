# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:12:59 2022

@author: acbaum1
"""
#quiz 5 
#creating the function
def convert_to_binary(number):
    numList=[]
    while number>0:
        numList.append(number%2)
        number=number//2
    return numList

#input a value from the user & call the function
num=int(input('Please provide a positive number:'))
binaryNum=convert_to_binary(num)

#create a loop to print
print('The binary equivalent of the number',num,'is',end=' ')
#choice 1: reverse the list and do print in for loop range (0,len)
for i in range (0,len(binaryNum)):
    print(binaryNum[i],end='')
    
#choice2: keep the list as is and do print in for loop range(len,-1,-1,-1)
for i in range(len(binaryNum)-1,-1,-1):
    print(binaryNum[i],end='')
