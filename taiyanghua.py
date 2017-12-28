# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 16:11:41 2017

@author: Administrator
"""

from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(179)
    if abs(pos())<1:
        break
end_fill()
done()