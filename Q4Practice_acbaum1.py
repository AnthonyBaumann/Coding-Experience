# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:41:43 2022

@author: acbaum1
"""

oddList=[]
evenList=[]

for i in range(10):
    num=int(input('Provide a whole number:'))
    if num%2==1:
        oddList.append(num)
    else:
        evenList.append(num)
        
        
print('you have entered these odd numbers:')
for i in range(0,len(oddList)):
    print(oddList[i],end=' ')
print('and they add up to be',sum(oddList))

print('You have entered these even numbers:')
for i in range(0,len(evenList)):
    print(evenList[i],end=' ')
print('and they add up to be',sum(evenList))