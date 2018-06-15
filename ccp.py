import numpy as np

a=np.arange(1,6)
b=a.clip(min=2)
print(b)
c=a.clip(max=2)
print(c)
d=a.clip(2,4)
print(d)
e=a.compress(a>=2)
print(e)
f=a.compress(a<=4)
print(f)
h=a.prod()
print(h)
i=a.cumprod()
print(i)
j=1
#用循环求阶乘
for k in range(2,11):
    j*=k
print(j)
#用递归求阶乘
def jiecheng(n):
    if n==1:
        return n
    return n*jiecheng(n-1)
print(jiecheng(10))
print((np.arange(10)+1).prod())
