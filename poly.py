import warnings
import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md
#去掉某些警告
warnings.filterwarnings('ignore',category=np.RankWarning)

#做预测的事情
def dmy2ymd(dmy):
    dmy=str(dmy,encoding='utf-8')
    date=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    ymd=date.strftime('%Y-%m-%d')
    return ymd

dates,bhp_closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/bhp.csv',\
            delimiter=',',usecols=(1,6),unpack=True,dtype=np.dtype('M8[D],f8'),\
            converters={1:dmy2ymd})

_,vale_closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/vale.csv',\
            delimiter=',',usecols=(1,6),unpack=True,dtype=np.dtype('M8[D],f8'),\
            converters={1:dmy2ymd})
#差价
diff_closing_prices=bhp_closing_prices-vale_closing_prices
days=dates.astype(int)
p=np.polyfit(days,diff_closing_prices,5)
#线的纵坐标
poly_closing_prices=np.polyval(p,days)

mp.figure("Polynomial Fitting",facecolor='lightgray')
mp.title('Polynomial Fitting',fontsize=20)
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
mp.scatter(dates,diff_closing_prices,c='limegreen',alpha=0.5,s=80,label='Difference Price')
mp.plot(dates,poly_closing_prices,c='dodgerblue',linewidth=3,label='Polynomail Fitting')
mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
