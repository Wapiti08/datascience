import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md
#做预测的事情
def dmy2ymd(dmy):
    dmy=str(dmy,encoding='utf-8')
    date=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    ymd=date.strftime('%Y-%m-%d')
    return ymd

dates,closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',\
            delimiter=',',usecols=(1,6),unpack=True,dtype=np.dtype('M8[D],f8'),\
            converters={1:dmy2ymd})

N=5
'''
计算原理
a b c d e f g?
aA+bB+cC = d \
bA+cB+dC = e  |-> A, B, C->g=dA+eB+fC
cA+dB+eC = f /                     
/ a b c \      / A \     / d \
| b c d  | X  |  B | =  |   e  |
\ c d e /      \ C /     \ f  /
---------     ------    ------
    a          x           b
x = np.linalg.lstsq(a, b)
g = x b
2N->2N+1
'''
pred_prices=np.zeros(closing_prices.size-2*N+1)
for i in range(pred_prices.size):
    a=np.zeros((N,N))
    for j in range(N):
        #取三个值，行与行之间进行卷积,a矩阵的赋值
        a[j,]=closing_prices[i+j:i+j+N]
    #b向量,N是三，下一行就是6，第一个数i=1
    b=closing_prices[i+N:i+N*2]
    x=np.linalg.lstsq(a,b)[0]
    #点乘
    pred_prices[i]=b.dot(x)
    print(a.dot(x),b,pred_prices[i])
mp.figure("Stack Price Prediction",facecolor='lightgray')
mp.title('Stock Price Prediction',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Price',fontsize=14)
ax=mp.gca()
#选择主定位器，用周做单位，然后用周一才标刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MONDAY))
#选择副定位器，用天做单位
ax.xaxis.set_minor_locator(md.DayLocator())
#选择格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates=dates.astype(md.datetime.datetime)
#存在的数据
mp.plot(dates,closing_prices,'o',c='lightgray',label='Closing Price')
#tseries.offsets----时间序列，时间增量，BDay----交易日
#date[-1]最后一个日子,加之后替换掉原来的数组
#append(arr, values, axis=None)
dates=np.append(dates,dates[-1]+pd.tseries.offsets.BDay())
#预测的图像,细节，这里是切片，是后面预测的数据，不然维数不相等
mp.plot(dates[2*N:],pred_prices,'o',c='orangered',label='Predicted Price')
mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
