i=0
while True:
    s=input("s=:")
    if s=='quit':
        break
    if len(s)<3:
        print('Sorry!')
        continue
    i+=1
    print('is',len(s))
print('i=',i)
print('Done!')