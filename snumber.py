def snmu(x):
    '''
    传入一个大于0的整数，返回从1累加到这个数的结果。
    :param x:
    :return y:
    '''
    if x < 0:
        print("请输入正确的数字，必须为大于0的整数。")
    elif x > 0:
        y = 0
        for i in range(1,x+1):
            y = y + i
    return y


#print(snmu(1000))


