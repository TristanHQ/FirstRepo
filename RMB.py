var = input("请输入带表示符号的人民币或美元（如30￥）：")
if var[-1] in ['￥']:
    s = float(var[:-1])/6.78
    print("%.2f$"%s)
elif var[-1] in ['B']:
    s = float(var[:-3])/6.78
    print("%.2fUSD"%s)
elif var[-1] in ['$']:
    r = (float(var[:-1]) )*6.78
    print("%.2f￥"%r)
elif var[-1] in ['D']:
    r = (float(var[:-3]) ) *6.78
    print("%.2fRMB"%r)
