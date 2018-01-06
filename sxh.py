while flag:
    for i in range(100,1000,1):
        if (i//100 + i%100//10 + i%10) == i:
            print(i)
