#算法题：输入n,假设n = 4
#10 11  12  1
#9  16  13  2
#8	15	14  3
#7  6   5   4

import numpy as np

n=int(input("请输入n的值："))
myArray=np.zeros((n,n),dtype=np.int16)
num=1
i=0
j=n-1
myArray[i][j]=1
while num<n*n:
    #向下走，行变大，列不变
    while(i+1<n and myArray[i+1][j]==0):
        i+=1
        num+=1
        myArray[i][j]=num   
    #向左走，行不变，列变小
    while(j-1>=0 and myArray[i][j-1]==0):
        j-=1
        num+=1
        myArray[i][j]=num
    #向上走，行变小，列不变
    while(i-1>=0 and myArray[i-1][j]==0):
        i-=1
        num+=1
        myArray[i][j]=num
    #向右走，行不变，列变小
    while(j+1<n and myArray[i][j+1]==0):
        j+=1
        num+=1
        myArray[i][j]=num
print(myArray)
    