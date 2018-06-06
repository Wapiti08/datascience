import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n=1000
#网格化
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
#以e为底的对数
z=(1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
ax=mp.gca(projection='3d')
mp.figure('3d surface',facecolor='gray')
mp.title('3d surface',fontsize=20)

ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)
ax.set_zlabel('z',fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_surface(x,y,z,rstride=5,cstride=5,cmap='jet')
mp.show()
