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

dates,closing_prices,volumes=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/bhp.csv',\
            delimiter=',',usecols=(1,6,7),unpack=True,dtype=np.dtype('M8[D],f8,f8'),\
            converters={1:dmy2ymd})
diff_closing_prices=np.diff(closing_prices)
# print(diff_closing_prices)
# sign_closing_prices=np.sign(diff_closing_prices)
sign_closing_prices=np.piecewise(diff_closing_prices,[diff_closing_prices<0,
            diff_closing_prices>0],[-1,1])
# print(sign_closing_prices)
#第二天才知道亏还是损
obvs=volumes[1:]*sign_closing_prices

#On-Balance Volume---净成交量
mp.figure("On-Balance Volume",facecolor='lightgray')
mp.title('On-Balance Volume',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('On-Balance Volume',fontsize=14)
ax=mp.gca()
#选择主定位器，用周做单位，然后用周一才标刻度
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MONDAY))
#选择副定位器，用天做单位
ax.xaxis.set_minor_locator(md.DayLocator())
#选择格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(axis='y',linestyle=':')
#这里是细节
dates=dates[1:].astype(md.datetime.datetime)
#存在的数据
rise=obvs>0
fall=obvs<0
#dates.size表示有这么多交易日，3f4每个颜色需要三个元素组合
fc=np.zeros(dates.size,dtype='3f4')
ec=np.zeros(dates.size,dtype='3f4')
fc[rise],fc[fall]=(1,0,0),(0,0.5,0)
#用白色表示边
ec[rise],ec[fall]=(1,1,1),(1,1,1)
#第四个参数表示底
mp.bar(dates,obvs,1.0,0,color=fc,edgecolor=ec,label='OBV')
mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
