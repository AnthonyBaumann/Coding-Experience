# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 09:35:41 2022

@author: acbaum1
"""

def min_max_avg(num1,num2,num3):
    numlist=[num1,num2,num3]
    mydict={}
    mydict['Max']=max(numlist)
    mydict['Min']=min(numlist)
    mydict['Average']=sum(numlist)/len(numlist)
    return mydict

num1=int(input('Provide number 1:'))
num2=int(input('Provide number 2:'))
num3=int(input('Provide number 3:'))

print(min_max_avg(num1, num2, num3))