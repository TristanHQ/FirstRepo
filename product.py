def product(*,x,y):
    s = 1
    for i in y:
        s = s*x*i
    return s


print(product(1,5,6))
