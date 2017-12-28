n = input("please enter a number:")
n = int(n)
s = '*'
for i in range(1,n+1,2):
    print('{0:^11}'.format(s*i))

