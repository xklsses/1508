##python算法题：输出2~100之间的素数  
i=2  
j=2  
##除了1和其本身，其他都不能整除  
for j in range(2,101):  
    for i in range(2,j):  
        if j%i==0:  
            break;  
        elif (j-1)==i:  
            print ('{}是素数'.format(j))  

