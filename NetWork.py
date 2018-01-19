#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time

PING_RESULT = 0
NETWORK_RESULT = 0

def DisableNetwork():
    ''' disable network card '''
    result = os.system(u"netsh interface set interface 以太网 disable")
    if result == 1:
        print("disable network card failed")
    else:
        print("disable network card successfully")

def EnableNetwork():
    ''' enable network card '''
    result = os.system(u"netsh interface set interface 以太网 enable")
    if result == 1:
        print("enable network card failed")
    else:
        print("enable network card successfully")

def ping():
    ''' ping www.baidu.com '''
    result = os.system(u"ping www.baidu.com")
    #result = os.system(u"ping www.baidu.com -n 3")
    if result == 0:
        print("ping www.baidu.com successfully")
        exit()
    else:
        print("ping www.baidu.com failed")
    return result


if __name__ == '__main__':
    while True:
        PING_RESULT = ping()

        if PING_RESULT == 0:
            time.sleep(60)
        else:
            DisableNetwork()
            time.sleep(10)

            EnableNetwork()
            time.sleep(30)
