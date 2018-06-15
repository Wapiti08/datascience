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

dates,bhp_closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/bhp.csv',\
            delimiter=',',usecols=(1,6),unpack=True,dtype=np.dtype('M8[D],f8'),\
            converters={1:dmy2ymd})

_,vale_closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/vale.csv',\
            delimiter=',',usecols=(1,6),unpack=True,dtype=np.dtype('M8[D],f8'),\
            converters={1:dmy2ymd})
#diff算数组中两个元素的差值，比原数组少一位
#np中数组除以数组,-1是最后一个元素，但是切片的后一位是不包括的，所以数据能对上
bhp_returns=np.diff(bhp_closing_prices)/bhp_closing_prices[:-1]
vale_returns=np.diff(vale_closing_prices)/vale_closing_prices[:-1]

#算数平均值
ave_a=np.mean(bhp_returns)
#离差
dev_a=bhp_returns-ave_a
#方差
var_a=np.mean(dev_a*dev_a)
#标准差
std_a=np.sqrt(var_a)
ave_b=np.mean(vale_returns)
dev_b=vale_returns-ave_b
var_b=np.mean(dev_b*dev_b)
std_b=np.sqrt(var_b)
#协方差
cov_aa=var_a
cov_ab=np.mean(dev_a*dev_b)
cov_ba=np.mean(dev_b*dev_a)
cov_bb=var_b
#相关性矩阵分子
covs=np.array([
    [cov_aa,cov_ab],
    [cov_ba,cov_bb]
])
print(covs)
#相关性矩阵分母
stds=np.array([
    [std_a*std_a,std_a*std_b],
    [std_b*std_a,std_b*std_b]
])
print(stds)
corr=covs/stds
print(corr)

corr=np.corrcoef(bhp_closing_prices,vale_closing_prices)
print(corr)


mp.figure("Returns",facecolor='lightgray')
mp.title('Returns',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Returns',fontsize=14)
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
mp.plot(dates[:-1],bhp_returns,c='orangered',label="BHP")
mp.plot(dates[:-1],vale_returns,c='dodgerblue',label="VALE")

mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
