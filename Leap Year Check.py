# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:05:09 2023

@author: talha.i
"""

#  Leap Year Check

year = int(input("Which year do you want to check? "))


# IF-ELSE CONDITIONS:
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")
    