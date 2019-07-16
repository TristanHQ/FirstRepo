# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 16:04:31 2019

@author:admin
"""
for j in range(1,5):
    for k in range(1,5):
        for l in range(1,5):
            if j != k and k !=l and j != l:
                print(j,k,l)