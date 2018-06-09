import numpy as np

#输出前面带有b代表的是utf-8：b'10-02-2011'
closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
                delimiter=',',usecols=(6),
                unpack=True)
                #用八个字节的数来表示日期，D表示以天为日期---M8[D]----只能识别年月日
mean=0
for closing_price in closing_prices:
    mean+=closing_price
# mean/=closing_prices.size
mean=closing_prices.sum()/closing_prices.size
print(mean)
#直接用函数
mean=np.mean(closing_prices)
print(mean)