# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:13:31 2019

@author: huanghuaqiao
"""

import jieba

txt = open("D:\\build\\雪中悍刀行.txt","r",encoding='utf-8').read()
name = ['徐凤年','徐骁','吴素','徐脂虎','徐渭熊','徐龙象','红薯','徐念凉','李淳罡','王仙芝','曹长卿','邓太阿','剑九黄','隋斜谷','李当心','韩生宣','轩辕敬城','张家圣人','白衣洛阳','轩辕青锋','吴六鼎','翠花','于新郎','楼荒','林鸦','王绣','王明寅']
words = jieba.lcut_for_search(txt)
counts={}

for n in name:
    for word in words:
         counts[word] = counts.get(word,0)+1
        
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(15):
    word,count =items[i]
    print("{0:<5}{1:>5}".format(word,count))
