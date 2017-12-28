# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:22:10 2017

@author: Administrator
"""

import turtle
import time
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)
turtle.done()