# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    'C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
    delimiter=',', usecols=(6), unpack=True)
# print(type(closing_prices))
#算数平均
mean=closing_prices.mean()
#离差,数组减一个数就是数组中所有元素-这个数
devs=closing_prices-mean
#离差方
sqrs=devs**2
#方差
svar=sqrs.mean()
#标准差
sstd=np.sqrt(svar)
print(sstd)


