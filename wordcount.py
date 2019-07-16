# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:37:53 2019

@author: huanghuaqiao
"""

import re #正则表达式
import collections #词频统计
import numpy as np #numpy数据处理库
import jieba #结巴分词
import wordcloud #词云展示
from PIL import Image #图像处理
import matplotlib.pyplot as plt #图像展示

fn = open('D:\\build\\雪中悍刀行.txt','r',encoding='utf-8')
st = open('D:\\build\\stopwords-master\\四川大学机器智能实验室停用词库.txt','r',encoding='utf-8')
string_data = fn.read()
stop_data = st.read()
fn.close()
st.close()

pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
string_data = re.sub(pattern,'',string_data)

seg_list_exact = jieba.cut(string_data,cut_all=False)
stop_list = jieba.cut(stop_data)
object_list = []
name_words  = ['徐凤年','徐骁','吴素','徐脂虎','徐渭熊','徐龙象','红薯','徐念凉','李淳罡','王仙芝','曹长卿','邓太阿','剑九黄','隋斜谷','李当心','韩生宣','轩辕敬城','张家圣人','白衣洛阳','轩辕青锋','吴六鼎','翠花','于新郎','楼荒','林鸦','王绣','王明寅']
#for n in neme_list:
#    remove_words.append(s)
#remove_words = [u'的',u'他',u'你',u'不',u'有',u'人',u'那',u'这',u'上',u'去',u'跟',u'要',u'笑',u'后',u'对',u'给',u'让',u'与',u'还',u'被',u'与',u'还',u'着',u'人',u'说',u'她',u'！',u'了',u'。',u'我',u'‘',u'“',u'”',u'，',u'和',u'在',u'都',u'就',u'也',u'我',u'？',u'：',u'是',u'道',u'没有',u'一个',u'不是',u'这个',u'不过',u'就是',u'什么',u'只是']

for word in seg_list_exact:
    if word in name_words:
        object_list.append(word)
        
word_counts = collections.Counter(object_list)
word_counts_top15 = word_counts.most_common(15)
print(word_counts_top15)

#mask = np.array(Image.open('D:\\build\\timg.jpg'))
wc = wordcloud.WordCloud(
        font_path = 'C:/Windows/Fonts/AdobeKaitiStd-Regular.otf',
#        mask=mask,
        max_words = 200,
        max_font_size = 100)

wc.generate_from_frequencies(word_counts)
#image_colors = wordcloud.ImageColorGenerator(mask)
#wc.recolor(color_func=image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()