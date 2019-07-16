# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:00:21 2019

@author: huanghuaqiao
"""

def jiecheng(*x):
    sum=1
    for i in x:
        sum=sum*i
    return sum


print(jiecheng(655,987,365,666,211,567))