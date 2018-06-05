import matplotlib.pyplot as mp
import numpy as np

n=10000
#产生均值为0，标准差为1的n个服从正太分布的随机数
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
d=np.sqrt(x**2+y**2)
#规定图的名称和颜色，整个框的名称
mp.figure('Scatter',facecolor='lightgray')
#规定框内图的名称
mp.title('Scatter',fontsize=20)
#规定x和y轴的名称和大小
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
#指定标签的大小
mp.tick_params(labelsize=10)
#加上网格，网格用点线
mp.grid(linestyle=':')
#d是距离值，介于0-1之间，cmap是颜色映射，jet从蓝到红，r是反过来
mp.scatter(x,y,s=60,c=d,cmap='jet_r',alpha=0.5)
mp.show()