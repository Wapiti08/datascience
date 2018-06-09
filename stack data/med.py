# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
closing_prices = np.loadtxt(
    'C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
    delimiter=',', usecols=(6), unpack=True)
#快速排序算法
sorted_prices=np.msort(closing_prices)
l=sorted_prices.size
median=(sorted_prices[int((l-1)/2)]+sorted_prices[int(l/2)])/2
print(median)
median=np.median(closing_prices)
print(median)


