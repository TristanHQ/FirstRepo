# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:25:41 2017

@author: Administrator
"""

sum,tmp = 0,1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("运算结果是：{}".format(sum))