L = []
def move(n,a,b,c):
    if n == 1:
        step = (a+str(n)+'-->'+c+str(n))
        L.append(step)
        return
    else:
        move(n-1,a,c,b)
        step = (a+str(n)+'-->'+c+str(n))
        L.append(step)
        move(n-1,b,a,c)

f = open("hnt.txt",'w')
move(5,'A','B','C')
f.write(str(L))
f = open("hnt.txt",'r')
s = f.readline()
print(s)
f.close()
