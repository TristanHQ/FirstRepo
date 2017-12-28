maxnum = input("请输入最大取值范围：")
maxnum = int(maxnum)
num = 1
i = 0
while 1 <= num < maxnum:
    if num == 1 or i == 1 or (num % i) == 0:
        num = num + 1
        i = i + 1
        continue
print(num)
