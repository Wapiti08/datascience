import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
import random

n_samples=100
#开始时所有的值用0来填
#其中2是两列的意思
data=np.zeros(n_samples,dtype=[
    ('position',float,2),
    ('size',float,1),
    ('growth',float,1),
    ('color',float,4)])
#R.uniform(a,b)	返回[a,b) 区间内的随机实数
data['position']=np.random.uniform(0,1,(n_samples,2))
data['size']=np.random.uniform(50,750,n_samples)
data['growth']=np.random.uniform(30,150,n_samples)
data['color']=np.random.uniform(0,1,(n_samples,4))
mp.figure('Bubble',facecolor='lightgray')
mp.title('Bubble',fontsize=20)
mp.xlabel('x',fontsize=14)
mp.ylabel('y',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
#一方面要变，同时还要把变化的值告诉函数
plot=mp.scatter(data['position'][:,0],data['position'][:,1],s=data['size'],c=data['color'])

#gcf获取当前图

#接收返回值以后就会变成进程级的返回值
def update(number):
    data['size']+=data['growth']
    #不能总让第一个破，所以循环让气泡从1-100循环破，使用模运算就行
    index=number%n_samples
    data['position'][index]=np.random.uniform(0,1,2)
    data['size'][index]=0
    data['growth'][index]=np.random.uniform(30.150)
    data['color'][index]=np.random.uniform(0,1,4)
    #变化后的信息都要告诉
    plot.set_offsets(data['position'])
    plot.set_sizes(data['size'])
    plot.set_colors(data[''color])


#需要接收返回值，不然返回值会随语句的执行而消失
anim=ma.FuncAnimation(mp.gcf(),update,interval=10)
mp.show()

