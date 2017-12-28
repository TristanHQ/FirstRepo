L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for i in L1:
    if isinstance (i,str)>0:
        L2.append(i)
L2=[s.lower() for s in L2]
print(L2)
