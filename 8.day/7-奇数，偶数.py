count = int(input("请输入一个数字"))
a = 0 #这是要求奇数的和
b = 0 #这是要求偶数的和
i = 0 
while i <= count:
	
	if i%2 ==0:
		b = b+i
	else:
		a = a+i
	i+=1
print("奇数和为:%d"%a)
print("基数和为:%d"%b)
print("总和为:%d"%(a+b))
