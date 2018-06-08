print("请输入星期几")
a = input("1星期一 2星期二 3星期三 4星期四 5星期五 6星期六 7星期七")
if a == "1" or "2" or "3" or "4" or "5":
	b = input("1上午 2下午")
	if b == "1":
		c =float(input("输入时间"))
		if c >8 and c<10:
			print("正在上课")
		if c >=10 and c<12:
			print("正在玩游戏")		
	if b == "2":
		d =float(input("输入时间"))
		if d >14 and d <15:
			print("正在上课")
	else :
		print("除非不知道在干什么")
elif a =="6":
	print("全天上课")
elif a =="7":
	print("逛街")
		 
