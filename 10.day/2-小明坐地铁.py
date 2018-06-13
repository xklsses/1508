a = 0
for i in range(1,33):
	for l in range(1,3):
		km =1000 
		if km <= 6:
			prize = 3
		elif km > 6 and km <=12:
			prize = 4
		elif km > 12 and km <=22:
			prize = 5
		elif km > 22 and km <=32:
			prize = 6
		elif km >32 :
			if (km -32)%20 == 0:
				prize = 6+(km-32)/20
			else:
				prize = 6+int((km-32)/20)+1
		if a >= 100 and a < 150:
				prize = prize *0.8
		elif a >= 150 and a <= 400:
				prize = prize *0.5
		elif a > 400:
				prize = prize
		a = a + prize 
print(a)
