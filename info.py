import keyword
path=('C://Users/huanghuaqiao/Desktop/')
fileName=('keyword.txt')
info=str(keyword.kwlist)
file=open(path+fileName,'w')
file.write(info)
file.close()
print("Done!")
