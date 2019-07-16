# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:08:26 2019

@author: huanghuaqiao
"""

import os

def DisableNetwork():
    '''禁用网卡'''
    result=os.system(u"netsh interface set interface 以太网 disable")
    if result == 1:
        print('禁用网卡失败！')
        input("Please Enter To Exit")
    else:
        print('禁用网卡成功！')
        input("Please Enter To Exit")
        
def EnableNetwork():
    '''启用网卡'''
    result=os.system(u"netsh interface set interface 以太网 enable")
    if result == 1:
        print('启用网卡失败！')
        input("Please Enter To Exit")
    else:
        print('启用网卡成功！')
        input("Please Enter To Exit")
        
def DisableWlan():
    '''禁用无线'''
    result=os.system(u"netsh interface set interface WLAN disable")
    if result == 1:
        print('禁用无线失败！')
        input("Please Enter To Exit")
    else:
        print('禁用无线成功！')
        input("Please Enter To Exit")
        
def EnableWlan():
    '''启用无线'''
    result=os.system(u"netsh interface set interface WLAN enable")
    if result == 1:
        print('启用无线失败！')
        input("Please Enter To Exit")
    else:
        print('启用无线成功！')
        input("Please Enter To Exit")
        
if __name__ == '__main__':
    print('------网卡选择工具------')
    print('------1.  禁用网卡------')
    print('------2.  启用网卡------')
    print('------3.  禁用无线------')
    print('------4.  启用无线------')
flag=True
while flag:
    Choice=input('请输入序号：')
    if Choice.isdigit()==False:
        print('输入有误，请输入数字序号！')
        continue
    elif Choice.isdigit()==True:
        Choice=int(Choice)
        if Choice==1:
            DisableNetwork()
            flag=False
        elif Choice==2:
            EnableNetwork()
            flag=False
        elif Choice==3:
            DisableWlan()
            flag=False
        elif Choice==4:
            EnableWlan()
            flag=False