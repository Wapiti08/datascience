import numpy as np

#randint是左闭右开
a=np.random.randint(10,100,27).reshape(3,3,3)
print(a)
b=a.max() #方法
print(b)
b=np.max(a) #函数
print(b)
e=np.min(a)
print(e)
f=a.ptp()
print(f)
g=np.ptp(a)
print(g)
#maximum只能在两个数组里面取
h=np.maximum(np.maximum(a[0],a[1]),a[2])
print(h)