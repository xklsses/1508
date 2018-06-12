import random
y = random.randint(1,100)
for i in range(1,101):
	i = int(input("请输入你想输入的值"))
	if i >y:
		print("输入值过大")
	elif i <y:
		print("输入值过小")
	else :
		if i ==y:
			print("恭喜你，猜对了")
		else :
			print("输入有误")

for l in range(10):
			break
