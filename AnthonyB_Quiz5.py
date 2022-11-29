# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:38:02 2022

@author: acbaum1
"""
bi_list=[]

num=int(input('Please provide a positive number:'))

def convert_to_binary(number_int):
    while num > 0:
        print(num % 2, end='')
        num=num//2
        bi_list.append(num)
    return binary_code

print('The binary equivalent of your number',(num),'is',(convert_to_binary(num)))

print('The binary equivalent of your number:')
for i in range(len(bi_listList)-1,-1,-1):
    print(Bi_List[i],end=' ')
    
