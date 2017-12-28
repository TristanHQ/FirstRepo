L = ['Bart','Lisa','Adam']
for name in L:
    print('Hello',name+'!')

print('*华丽的分界线*')

for name in L:
    print('Hello,%s!' % name)

print('*华丽的分界线*')

i = 0
while i < 3:
    print('Hello',L[i]+'!')
    i = i + 1
