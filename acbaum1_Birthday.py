# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime as dt

dayBorn=int(input('What day of the month were you born?:'))
monthBorn=int(input('What month were you born?:'))
yearBorn=int(input('What year were you born?:'))

db=dt.date(yearBorn,monthBorn, dayBorn)


if __name__!= '__main__':
        dbFormatted=db.strftime("%d of %B, on a %A, in %Y")
        print('\nYou were born on the', dbFormatted)
        