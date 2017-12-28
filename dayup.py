n = input("please enter a number:")
n = float(n)
s = 1
up = (s + n*0.001)**365
down = (s-n*0.001)**365
print("{:.2f},{:.2f},{}".format(up,down,int(up//down)))
