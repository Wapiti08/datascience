#vwap(volume---成交量 weighted Average Price,成交量加权平均值)
import numpy as np
import datetime as dt

def dmy2days(dmy):
    dmy=str(dmy,encoding='utf-8')
    date=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    days=(date-dt.date.min).days
    return days


#输出前面带有b代表的是utf-8：b'10-02-2011'
days,closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
                delimiter=',',usecols=(1,6),
                unpack=True,converters={1:dmy2days})
#用八个字节的数来表示日期，D表示以天为日期---M8[D]----只能识别年月日

twap, sw = 0, 0

for closing_price,day in zip(closing_prices,days):
    twap+=closing_price*day
    sw+=day
twap/=sw
print(twap)
#做点乘
twap=closing_prices.dot(days)/days.sum()
print(twap)
twap=np.average(closing_prices,weights=days)
print(twap)