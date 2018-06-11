#电脑 用户

import random
#i = 0
p = random.randint(1,100)
while True: 
	y = int(input("请输入1,100之间的数"))
	if y > p:
		print("所输入的值过大")
	elif y < p:
		print("所输入的值过小")
	elif y == p:
		print("恭喜你猜对了")
		break
	#i+=1
