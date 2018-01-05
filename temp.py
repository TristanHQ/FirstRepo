var = input("请输入带表示符号的温度（如C30）：")
if var[0] in ['C','c']:
    f = 1.8 * float(var[1:]) + 32
    print("F%.2f"%f)
elif var[0] in ['F','f']:
    c = (float(var[1:]) - 32) / 1.8
    print("C%.2f"%c)