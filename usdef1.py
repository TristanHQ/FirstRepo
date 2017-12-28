def tocn(x):
    if isinstance(x,int) == False and isinstance(x,float) == False:return
    x = str(x)
    if len(x) == 0:return
    y = []
    dist = {0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
    for n in x:
        for i,j in dist.items():
#            print(n,type(n),i,type(i),j,type(j))
            if int(n) == i:
                y.append(j)
    return y

print(tocn(12345))