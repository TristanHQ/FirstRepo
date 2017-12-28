def opter(a,b,c):
    if b =='+':
        return a+c
    if b =='-':
        return a-c
    if b =='*':
        return a*c
    if b =='/':
        return a/c


print(opter(10,'+',20),opter(99,'-',88),opter(11,'*',22),opter(99,'/',33))