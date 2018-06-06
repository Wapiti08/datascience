import numpy as np
import matplotlib.pyplot as mp

n=1000
#网格化
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
#以e为底的对数
z=(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
mp.figure('Hot', facecolor='lightgray')
mp.title('Hot', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.grid(linestyle=':')

#low表示垂直抽象由底到高，默认是反的
mp.imshow(z,cmap='jet',origin='low')
#给z轴的线添加标签
mp.colorbar().set_label('z',fontsize=14)
mp.show()

