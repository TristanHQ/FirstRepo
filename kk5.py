y=int(input("please input the year:"))
if y%4==0:
    print("This year is leap year")
elif y%400==0:
    print("This year is leap year")
else:
    print("This year is common year")
