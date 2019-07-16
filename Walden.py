#_*_ encoding:utf-8 _*_
import string

path='d:\\build\Walden.txt'

with open(path,'r')as txt:
    words=[raw_word.strip(string.punctuation).lower() for raw_word in txt.read().split()]
    words_index=set(words)
    counts_dict={index:words.count(index) for index in words_index}

for word in sorted(counts_dict,Key=lambda x:counts_dict[x],reversed=True):
    print('{}--{} times'.format(word,counts_dict[word]))

