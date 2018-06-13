#import random 
a = 0
for i in range(1,33):
	for l in range(1,3):
		#km = random.randint(1,100)
        km = 52
		if km <=6:
			price = 3
		elif km > 6 and km <=12:
			price = 4
		elif km > 12 and km <=22:
			price = 5
		elif km > 22 and km <=32:
			price = 6
		elif km > 32:
			price = 6+int((km-32)/20)+1
		if a >=100 and a < 150 :
			price = price * 0.8
		elif a >=150 and a < 400:
			price = price *0.5
		elif a > 400 :
			price = price * 1
		a = a+price 
print("输出%.02f"%a)	
