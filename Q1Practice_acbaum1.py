# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 09:33:10 2022

@author: acbaum1
"""
num1=int(input("Integer One: "))
num2=int(input("Integer Two: "))
num3=int(input("Integer Three: "))

num_list=[num1,num2,num3]

ave=(sum(num_list)/len(num_list))
minimum=min(num_list)
maximum=max(num_list)

resultsDict={"Average":ave, "Minimum":minimum, "Maximum":maximum}

print('The average of the three numbers is:', resultsDict["Average"])
print('The minimum value of the three numbers is:', resultsDict["Minimum"])
print('The maximum value of the three numbers is:', resultsDict["Maximum"])