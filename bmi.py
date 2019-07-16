height=input('输入身高(米)：')
weight=input('输入体重（千克）：')
h=float(height)
w=float(weight)
bmi=w/(h**2)
if bmi<18.5:
    print('过轻')
elif 18.5<=bmi<=25:
    print('正常')
elif 25<=bmi<=28:
    print('过重')
else:
   print('严重肥胖')  
pass
print