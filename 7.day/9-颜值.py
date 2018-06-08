print("选择你的性别")
a = input("1男 2女")
if a =="1":
	s =int(input("请输入身高"))
	c =int(input("请输入财富"))
	y =int(input("请输入颜值"))
	if s>180 and c>1000 and y>90:
		print("高富帅")
	else:
		print("稳住，别哭")
if a =="2":
	p = input("请输入皮肤颜色")
	m =int(input("请输入财富"))
	o =int(input("请输入颜值"))
	if p=="白色" and m>800 and o>90:
		print("白富美")
	else:
		print("哈哈哈")
