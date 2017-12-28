'''str1=input("请输入一个人的名字：")
str2=input("请输入一个国家的名字：")
print("世界这么大，{}想去{}看看。".format(str1,str2))
'''
n = input("请输入一个整数：")
s = 0
n = int(n)+1
for i in range(n):
    s = s + i
print("0到"+str(n-1)+"求和结果为：", s)
