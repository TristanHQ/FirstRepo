bill = 700000000000
count = 0

def as_num(x):
    y='{:.5f}'.format(x) # 5f表示保留5位小数点的float型
    return(y)
    
while bill >0.02:
    bill = bill/2
    count = count+1
    print(count,as_num(bill))
print(count)
