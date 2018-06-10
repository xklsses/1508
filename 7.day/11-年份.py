a = int(input("请输入年份"))

b = a%4
c = a%100
d = a%400
if b == 0 and c != 0 or d == 0: 
	print('闰年')
else:
	print('平年')

