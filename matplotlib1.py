import numpy as np
import matplotlib.pyplot as plt

#作图的变量自变量
x=np.linspace(0,10,1000)
#因变量y
y=np.sin(x)+1
#因变量z
z=np.cos(x**2) +1

#设置图像大小
plt.figure(figsize=(8,4)) 
#作图，设置标签,线条颜色，线条大小
plt.plot(x,y,label='$\sin x+1$',color='red',linewidth=2)
#作图，设置标签，线条标签
plt.plot(x,z,'b--',label='$\cos x^2+1$')
#x轴名称
plt.xlabel('Time(s) ')
#y轴名称
plt.ylabel('Volt')
#标题
plt.title('A Simple Example')
#显示的y轴范围
plt.ylim(0,2.2)
#显示图例
plt.legend()
#显示作图效果
plt.show()