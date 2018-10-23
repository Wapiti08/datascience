import numpy as np
import matplotlib.pyplot as mp

n=12
x=np.arange(n)
y1=(1-x/n)*np.random.uniform(0.5,1.0,n)
y2=(1-x/n)*np.random.uniform(0.5,1.0,n)

mp.figure('Bar',facecolor='lightgray')
mp.title('Bar',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.xticks(x,x+1)
mp.tick_params(labelsize=10)
#only x axis
mp.grid(axis='y',linestyle=':')
#ec边缘色，fc填充色
mp.bar(x,y1,0.5,ec='white',fc='dodgerblue',label='Sample 1')
for _x,_y in zip(x,y1):
    #ha水平居中方式,va垂直方向贴着矩形区域的底
    mp.text(_x,_y,'%.2f'%_y,ha='center',va='bottom',size=8)
mp.bar(x,-y2,ec='white',fc='dodgerblue',alpha=0.5,label='Sample 2')
for _x,_y in zip(x,y2):
    #ha水平居中方式,va垂直方向，拿矩形区域的顶去对
    mp.text(_x,-_y,'%.2f'%_y,ha='center',va='top',size=8)
mp.legend()
mp.show()
