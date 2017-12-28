#coding = utf-8
n = input('please input the number of Successione di Fibonacci ')
n = int(n)
F=[0,1]
for i in range(n):
    temp = F[i]+F[i+1]
    F.append(temp)
    print(F)
