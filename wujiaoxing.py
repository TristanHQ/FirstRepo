# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:43:19 2017

@author: Administrator
"""

from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
    
end_fill()
done()