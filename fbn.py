n= eval(input("please input number:"))
f0=0
f1=1
if n <= 2:
    print(f0,f1)
elif n >2:
    print(f0)
    print(f1)
    for i in range(n-2):
        f2=f0+f1
        f0=f1
        f1=f2
        print(f2)
else:
    print("Done!")