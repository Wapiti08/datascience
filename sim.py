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

dates,opening_prices,highest_prices,\
            lowest_prices,closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/bhp.csv',\
            delimiter=',',usecols=(1,3,4,5,6),unpack=True,\
            dtype=np.dtype('M8[D],f8,f8,f8,f8'),\
            converters={1:dmy2ymd})

def profit(opening_price,highest_price,lowest_price,closing_price):
    buying_price=opening_price*0.9985
    #价格要出现过才能买进
    if lowest_price<=buying_price<=highest_price:
        return (closing_price-buying_price)*100/buying_price
    #返回一个无效值
    return np.nan
#profits=np.vertorize(profit)得到的是一个函数
profits=np.vectorize(profit)(opening_prices,highest_prices,\
    lowest_prices,closing_prices)
#返回无效值
nan=np.isnan(profits)
#~取反
dates,profits=dates[~nan],profits[~nan]
gain_dates,gain_profits=\
    dates[profits>0],profits[profits>0]
loss_dates,loss_profits=\
    dates[profits<0],profits[profits<0]


mp.figure("Trading Simulation",facecolor='lightgray')
mp.title('Trading Simulation',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Profit',fontsize=14)
ax=mp.gca()
#选择主定位器，用周做单位，然后用周一才标刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MONDAY))
#选择副定位器，用天做单位
ax.xaxis.set_minor_locator(md.DayLocator())
#选择格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(axis='y',linestyle=':')
if dates.size>0:
    dates=dates.astype(md.datetime.datetime)
    mp.plot(dates,profits,c='gray',label='Profit')
    #画一条水平线
    mp.axhline(y=profits.mean(),linestyle=':',color='gray')
#赚得的收益
if gain_dates.size>0:
    gain_dates=gain_dates.astype(md.datetime.datetime)
    mp.plot(gain_dates,gain_profits,'o',c='orangered',label='Gain Profit')
    #画一条水平线
    mp.axhline(y=gain_profits.mean(),linestyle=':',color='orangered')
#损失的利润
if loss_dates.size>0:
    loss_dates=loss_dates.astype(md.datetime.datetime)
    mp.plot(loss_dates,loss_profits,'o',c='dodgerblue',label='Loss Profit')
    #画一条水平线
    mp.axhline(y=loss_profits.mean(),linestyle=':',color='dodgerblue')

mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
