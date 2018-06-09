#vwap(volume---成交量 weighted Average Price,成交量加权平均值)
import numpy as np


#输出前面带有b代表的是utf-8：b'10-02-2011'
closing_prices,volumes=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
                delimiter=',',usecols=(6,7),
                unpack=True)
                #用八个字节的数来表示日期，D表示以天为日期---M8[D]----只能识别年月日
#sw为权重之和
vwap,sw=0,0
for closing_price,volume in zip(closing_prices,volumes):
    vwap+=closing_price*volume
    sw+=volume
vwap/=sw
print(vwap)
#做点乘
vwap=closing_prices.dot(volumes)/volumes.sum()
print(vwap)
vwap=np.average(closing_prices,weights=volumes)
print(vwap)