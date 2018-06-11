# 1:石头 2:剪刀 3:布
import random
while True:
	c = random.randint(1,3)
	player = int(input("请输入1:石头 2:剪刀 3:布"))
	if (player==1 and c==2) or (player==2 and c==3) or (player==3 and  c==1 ):
		print("你赢了")
	elif player == c:
		print("平局")
	else:
		print("你输了")
	if player == 0:
		print("退出成功")
		break

