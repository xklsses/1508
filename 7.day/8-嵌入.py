print("欢迎来到游戏世界\n请选择你的游戏")
a = input("1.穿越火线 2.贪吃蛇:")
account = "1538444890"
pwd = "123456"
if a == "1":
	acc = input("请输入你的账号")
	p = input("请输入你的密码")
	if acc ==account and p ==pwd:
		print("登录成功\n祝你游戏愉快")
	else:
		print("登录失败")
elif a == "2":
     print("欢迎来到贪吃蛇\n祝你游戏愉快")
else:
     print("没有这款游戏。再见")    



	


 

