# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:40:24 2022

@author: acbaum1
"""

def fibonacci(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        fibList=[0,1]
        for i in range(n-1):
            nth=fibList[0]+fibList[1]
            fibList[0]=fibList[1]
            fibList[1]=nth
    return fibList[1]

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')