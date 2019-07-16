#_*_ encoding: UTF-8_*_
passWord_List=['*#*#','12345']
def account_login():
	passWord=input('请输入密码:')
	passWord_correct=passWord==passWord_List[-1]
	passWord_reset=passWord==passWord_List[0]
	if passWord_correct:
		print('登录成功！')
	elif passWord_reset:
		new_Password=input("请输入一个新的密码：")
		passWord_List.append(new_Password)
		print("你的密码修改成功！")
		account_login()
	else:
		print("密码错误或输入错误！")
		account_login()
account_login()