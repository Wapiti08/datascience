import numpy as np

def fun(a,b,c):
    d=a+b+c
    e=a*b*c
    return d,e

A=np.array([1,3,5,7])
B=np.array([2,4,6,8])
C=np.array([0,1,2,3])
#变成矢量函数
vfun=np.vectorize(fun)
D,E=vfun(A,B,C)
print(D,E)


