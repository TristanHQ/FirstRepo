m = input("m =")
n = input("n =")
if "." in m:
    m = float(m)
else:
    m = int(m)
n = int(n)
print((m+n),(m*n),(m**n),(m%n),(max(m,n)))