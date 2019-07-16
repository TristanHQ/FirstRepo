# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:55:28 2019

@author: huanghuaqiao
"""
import time as t
start = t.clock()
def fact_iter(num,product):
    if num ==1:
        return product
    return fact_iter(num -1,num * product)
    

def fact(n):
    return fact_iter(n,1)
end = t.clock()
print(fact(1000))
print(end-start)