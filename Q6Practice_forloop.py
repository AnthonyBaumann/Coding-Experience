# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:11:21 2022

@author: acbaum1
"""

def min_max_avg(num1,num2,num3):
    numlist=[num1,num2,num3]
    mydict={}
    mydict['Max']=max(numlist)
    mydict['Min']=min(numlist)
    mydict['Average']=sum(numlist)/len(numlist)
    return mydict
inputList=[]
for f in range(3):
    num=float(input('Provide a number:'))
    inputList.append(num)

print(min_max_avg(inputList[0],inputList[1],inputList[2]))