def newFile():
    import os
    path=("C://Users/huanghuaqiao/Desktop/New/")
    if os.path.exists(path) is False:
        os.makedirs(path)
    for i in range(1,11):
        fileName=(path+str(i)+'.txt')
        file=open(fileName,'w')
        file.write(str(i))
        file.close()
        print('File'+' '+ str(i)+ ' '+ 'Write is Done!')

newFile()


