#-*-coding:utf-8-*-
print("     *****地铁乘车消费计算计算器*****")
distance = input("请输入您乘车区间的距离,距离大于0：")   #输入每天去公司乘坐地铁的距离（公里）
if distance ==0:
    print("您还是在原地呆着吧")
    exit()
cost = 0.0                                          #设置变量cost记录用户在地铁上的消费情况（元）
day = 1                                             #设置变量记录天数
#while day<=20:
while day<=40:                                      #共20天，来回一共40趟
    rate = 0.0                                      #设置优惠率
#   i = 1                                           #设置while循环，当天数大于20时结束循环
#   while i<=2:                                     #设置内嵌while循环，分别计算来回的消费情况，同样的乘车区间来回的消费可能不一样
    if cost>=100 and cost<150:                      #设置if-elif-else语句判断当前消费情况，并设置变量记录优惠率
        rate = 0.8
    elif cost>=150 and cost<400:
        rate = 0.5
    else :
        rate = 1.0
    if distance<=6:                                 #使用if-elif-else语句判断用户的乘车区间，同时在总消费上增加相应费用乘上优惠率
        cost+=(3*rate)
    elif distance>6 and distance<=12:
        cost+=(4*rate)
    elif distance>12 and distance<=22:
        cost+=(5*rate)
    elif distance>22 and distance<=32:
        cost+=(6*rate)
    else :                                          #乘车超过32公里时候的计算公式
        if (distance-32)%20==0:
            cost+=((6+(distance-32)/20)*rate)
        else:
            cost+=((6+(distance-32)/20+1)*rate)
    day+=1
print("您当月在地铁上的花费为%.2f"%cost)               #输出花费(元),保留两位小数
