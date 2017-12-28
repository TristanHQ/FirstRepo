# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:39:31 2017

@author: Administrator
"""

diet =['西红柿','花椰菜','黄瓜','牛肉','鲤鱼']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))