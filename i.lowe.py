L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for i in L1:
    if isinstance (i,str):
        L2.append(i.lower())
print(L2)
