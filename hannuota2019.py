# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:51:57 2019

@author: huanghuaqiao
"""

def move(n,a,b,c):
    if n ==1:
        print(a,'----->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
move(2,'A','B','C')