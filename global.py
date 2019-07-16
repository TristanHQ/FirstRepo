# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:32:15 2019

@author: huanghuaqiao
"""

x = 50
def funcA():
    global x
    print('x is',x)
    x=2
    print('Changed global x to',x)
    
    
funcA()
print('Value of x is',x)