s1 = 72
s2 = 85
r = (int(s1)-int(s2))/int(s1)*100
if int(r) <= 0:
    print('小明成绩相对于去年提升了%.01f %%' % (-r))
else:
    print('小明成绩相对于去年提升了%.01f %%' % r)
input('plese enter to exit')
