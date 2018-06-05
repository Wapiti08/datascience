import numpy as np
import matplotlib.pyplot as mp

n=1000
x=np.linspace(0,8*np.pi,n)
sin_y=np.sin(x)
cos_y=np.cos(x/2)/2

mp.figure('Fill',facecolor='lightgray')
mp.title('Fill',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
#设置图例格式
mp.plot(x,sin_y,c='dodgerblue',label=r'$y=sin(x)$')
mp.plot(x,cos_y,c='red',label=r'$y=\frac{1}{2}con(\frac{x}{2})$')
mp.fill_between(x,cos_y,sin_y,cos_y<sin_y,color='dodgerblue',alpha=0.5)
#显示图例
mp.legend()
mp.show()