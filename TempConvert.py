# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:05:23 2017

@author: Administrator
"""
#TempConvert.py
while True:
    val = input("请输入带温度表示符号的温度值（例如：30C）:")
    if val[-1] in ['C','c']:
        f = 1.8 * float(val[0:-1]) + 32
        print("转换后的温度为：%.2fF"%f)
    elif val[-1] in ['F','f']:
        c = (float(val[0:-1]) - 32) / 1.8
        print("转换后的温度为：%.2fC"%c)
    else:
        print("输入有误")
