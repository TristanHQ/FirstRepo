flag = 10
while flag <= 10 and flag >0:
    number = 23
    guess = input('猜数字，你有{}次机会，请输入一个整数: '.format(flag))
    guess = int(guess)
    if guess == number:
        # 新块从这里开始
        print('恭喜你猜对了！')
        print('(但是你没有获得任何奖品。)')
        break
        # 新块在这里结束
    elif guess < number:
        # 另一代码块
        print('不对, 比这个数字高一些。')
        flag -=1
        continue
        # 你可以在此做任何你希望在该代码块内进行的事情
    else:
        print('不对, 比这个数字低一些。')
        # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
        flag -=1
        continue
print('完成！')
# 这最后一句语句将在
# if 语句执行完毕后执行。