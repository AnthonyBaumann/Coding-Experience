# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:36:55 2022

@author: acbaum1
"""
import math

def sum_product_sqrtsq(num_1,num_2):
    num_list=[num_1,num_2]
    mydict={}
    mydict['Sum']=sum(num_list)
    mydict['Product']=(num_1*num_2)
    mydict['diagonal']= round(math.sqrt(num_1**2+num_2**2),3)
    return mydict

if __name__=='__main__':

    inputList=[]
    for f in range(2):
        num=int(input('Provide a whole number:'))
        inputList.append(num)

print(sum_product_sqrtsq(inputList[0],inputList[1])) 