# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:43:15 2019

@author: huanghuaqiao
"""

def getLen(x):
    s=0
    for i in x:
        s+=1
    return s

#x='1','2','3','4','5'
x=1,2,3,4,5,6,7
#result=getLen(x)
print(getLen(x))
#print(len(x))
#s=0
#for i in x:
#    s+=1
#    print(i)
#print('\n',s)