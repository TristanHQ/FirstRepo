f = open("hnt.txt",'w+')
def move(n,a,b,c):
    if n == 1:
        step = (a+str(n)+'-->'+c+str(n)+'\n')
#        L.append(step)
        f.write(step)
        return
    else:
        move(n-1,a,c,b)
        step = (a+str(n)+'-->'+c+str(n)+'\n')
#        L.append(step)
        f.write(step)
        move(n-1,b,a,c)


move(5,'A','B','C')
#f.write(str(L))
f = open("hnt.txt",'r')
s = f.read()
print(s)
f.close()
