import datetime as dt
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import matplotlib.dates as md
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
#diff算数组中两个元素的差值，比原数组少一位
#np中数组除以数组,-1是最后一个元素，但是切片的后一位是不包括的，所以数据能对上
bhp_returns=np.diff(bhp_closing_prices)/bhp_closing_prices[:-1]
vale_returns=np.diff(vale_closing_prices)/vale_closing_prices[:-1]

#用窗函数做卷积来平滑函数，从第八个交易日开始
N=8
#得到一个关于y轴的对称值，这些值是余弦函数，用来作为权值
weights=np.hanning(N)
#先把权之和在这里除了
weights/=weights.sum()
#convolve第二个参数是下标
bhp_smooth_returns=np.convolve(bhp_returns,weights,'valid')
vale_smooth_returns=np.convolve(vale_returns,weights,'valid')

#多项式曲线拟合求交点
#将日期转化未数字
days=dates[N-1:-1].astype(int)
#阶数
degree=5
#求系数
bhp_p=np.polyfit(days,bhp_smooth_returns,degree)
#求y坐标
bhp_poly_returns=np.polyval(bhp_p,days)
#求系数
vale_p=np.polyfit(days,vale_smooth_returns,degree)
#求y坐标
vale_poly_returns=np.polyval(vale_p,days)

#求两个数组的差
sub_p=np.polysub(bhp_p,vale_p)
#求f(x)=0的解，即交点的横坐标
roots=np.roots(sub_p)
#求实根
reals=roots[np.isreal(roots)].real
inters=[]
for real in reals:
    #首先应该在日期的范围之内：
    if days[0]<=real and real <=days[-1]:
        #求出交点的坐标，加到inters中去
        inters.append([real,np.polyval(bhp_p,real)])
#给交点排个序
inters.sort()
#变成数组
inters=np.array(inters)
print(inters)

mp.figure("Smoothing Returns",facecolor='lightgray')
mp.title('Smoothing Returns',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Smoothing Returns',fontsize=14)
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
#不平滑的收益率
mp.plot(dates[:-1],bhp_returns,c='orangered',alpha=0.25,label="BHP")
mp.plot(dates[:-1],vale_returns,c='dodgerblue',alpha=0.25,label="VALE")

#平滑的收益率,下标n-1表示第n个元素
mp.plot(dates[N-1:-1],bhp_smooth_returns,c='orangered',label="Smooth_BHP")
mp.plot(dates[N-1:-1],vale_smooth_returns,c='dodgerblue',label="Smooth_VALE")

#多项式拟合函数曲线
mp.plot(dates[N-1:-1],bhp_poly_returns,c='orangered',linewidth=3,alpha=0.75,label="Poly_BHP")
mp.plot(dates[N-1:-1],vale_poly_returns,c='dodgerblue',linewidth=3,alpha=0.75,label="Poly_VALE")

dates,returns=np.hsplit(inters,2)
#变成matplotlib类型
# dates1=dates.astype(int)
# dates2=dates.astype(int).astype('M8[D]')
dates=dates.astype(int).astype('M8[D]').astype(md.datetime.datetime)
# print(dates1)
# print(dates2)
# print(dates)
#c表示color，marker表示图标，s大小，zorder叠加次序，越大越上层
mp.scatter(dates,returns,marker='x',c='firebrick',s=120,lw=3,zorder=3)

mp.legend()
#日期自动倾斜，防止叠加
mp.gcf().autofmt_xdate()
mp.show()
