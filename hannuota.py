def move(n,a,b,c):
    if n == 1:
        print(a+str(n)+'-->'+c+str(n))
        return
    else:
        move(n-1,a,c,b)
        print(a+str(n)+'-->'+c+str(n))
        move(n-1,b,a,c)

move(10,'A','B','C')