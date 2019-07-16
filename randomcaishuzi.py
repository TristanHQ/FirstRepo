# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:08:57 2019

@author: huanghuaqiao
"""

import random
count=10
result=random.randint(1,100)
while count >0:
    begin=print("猜数字游戏，你有"+str(count)+"次机会")
    print("*"*30)
    guess=input("请输入你猜测的结果：")
    guess=int(guess)
    if guess==result:
        print("恭喜你猜对了！但是没有奖品哦。。")
        break
    elif guess>result:
        print("不对，比这个数字小一些。")
    elif guess<result:
        print("不对，比这个数字大一些。")
    count-=1