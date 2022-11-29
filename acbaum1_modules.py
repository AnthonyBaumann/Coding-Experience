# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:05:14 2022

@author: acbaum1
"""

import acbaum1_Birthday

print('\n\nNow lets talk about your major.')

majorAbbr= input('Pick any of the following: CS, GIS, IS, HIM, SRE, or NA:')

if majorAbbr == 'CS':
    major='Computer Science'
if majorAbbr == 'GIS':
    major='Geographic Information Systems'
if majorAbbr == 'IS':
    major='Information Systems'
if majorAbbr == 'HIM':
    major='Health Informatics and Management'
if majorAbbr == 'SRE' :
    major= 'Sustainable and Renewable Energy'
if majorAbbr == 'NA':
    major='Ungergraduate College'

print('\nYou\'re majoring in',major,'.')