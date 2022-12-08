# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:41:31 2022

@author: acbaum1
"""
import math 

def squaredList(aList):
    sqrlist=[]
    for i in aList:
        sqrlist.append(math.pow(i,2))
    return sqrlist
    
if __name__=='__main__':  
    user_val=input('Enter your numbers seperated by a space:')
    numList=[int(i) for i in user_val.split()]
    newList=squaredList(numList)
    
    print("The squared numbers are:")
    for num in newList:
        print(num)
    
