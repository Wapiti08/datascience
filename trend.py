import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md

#数据是一家上市公司的股票跌涨情况示意图
def dmy2ymd(dmy):
    #str（）函数会让每个字符占四字节，达到统一的效果，
    # 要让str函数理解之前的字符是啥需要加个编码方式来说明
    #utf-8--->ucs-4
    dmy=str(dmy,encoding='utf-8')
    #str,parse,time,data()---只要年月日
    date=dt.datetime.strptime(dmy,'%d-%m-%Y').date()
    #format--格式化
    ymd=date.strftime('%Y-%m-%d')
    return ymd

#输出前面带有b代表的是utf-8：b'10-02-2011'
dates,opening_prices,highest_prices,lowest_prices,\
closing_prices=np.loadtxt('C:/Users/Lenovo/Desktop/AI/datascience/Day01/Day01/MW/DS/data/aapl.csv',
                delimiter=',',usecols=(1,3,4,5,6),
                unpack=True,dtype=np.dtype('M8[D],f8,f8,f8,f8'),
                converters={1:dmy2ymd})
                #用八个字节的数来表示日期，D表示以天为日期---M8[D]----只能识别年月日
#基准点
trend_points=(highest_prices+lowest_prices+closing_prices)/3
spreads=highest_prices-lowest_prices
#压力线
resistance_points=trend_points+spreads
#支撑线
support_points=trend_points-spreads

days=dates.astype(int)
#ones_like像什么一样，维度一致,column_stack---列合并
a=np.column_stack((days,np.ones_like(days)))

#取第零行元素，后面的残差，标准差省略
x=np.linalg.lstsq(a,trend_points)[0]
#取到的第一行元素中，第一个是斜率，第二个是坐标
trend_line=days*x[0]+x[1]

#求压力线的横坐标
x=np.linalg.lstsq(a,resistance_points)[0]
#取到的第一行元素中，第一个是斜率，第二个是坐标
resistance_line=days*x[0]+x[1]

#求趋势线的横坐标
x=np.linalg.lstsq(a,support_points)[0]
#取到的第一行元素中，第一个是斜率，第二个是坐标
support_line=days*x[0]+x[1]

a=days,np.ones_like(days)
mp.figure('Trend',facecolor='lightgray')
mp.title('Trend',fontsize=20)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Price',fontsize=14)
ax=mp.gca()
#水平轴设置,主定位器，Week。以星期为间隔单位
ax.xaxis.set_major_locator(
        md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
#格式化器,日子的格式，月份的格式，年的格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates=dates.astype(md.datetime.datetime)
#收盘价-开盘价 这两个结果可以作为掩码
rise=closing_prices-opening_prices>=0.01
# print("rise:",rise)
fall=opening_prices-closing_prices>=0.01
#这里的3表示三个数
fc=np.zeros(dates.size,dtype='3f4')
# print("fc:",fc)
ec=np.zeros(dates.size,dtype='3f4')
#作为一个筛子，把真值筛选出来,阴阳两线进行填充
#前景色,用布尔型数组作为另一个数组的下标
#所有为true的元素都是可以访问的，所有为假的元素都被隐藏
fc[rise],fc[fall]=(1,1,1),(0.85,0.85,0.85)
# print(fc)
#背景色
ec[rise],ec[fall]=(0.85,0.85,0.85),(0.85,0.85,0.85)
#引线是最高价-最低价
mp.bar(dates,highest_prices-lowest_prices,0,lowest_prices,color=fc,edgecolor=ec)
#opening_prices-----作为底
mp.bar(dates,closing_prices-opening_prices,0.8,opening_prices,color=fc,edgecolor=ec)
#解决日期重复的问题
#s大小
mp.scatter(dates,trend_points,c='dodgerblue',alpha=0.5,s=80,zorder=2)
#压力点
mp.scatter(dates,trend_points,c='orangered',alpha=0.5,s=80,zorder=2)
#支撑点
mp.scatter(dates,resistance_points,c='limegreen',alpha=0.5,s=80,zorder=2)

#趋势线
mp.plot(dates,trend_line,c='dodgerblue',linewidth=3,label='Trend')
#压力线
mp.plot(dates,resistance_line,c='orangered',linewidth=3,label='Resistance')
#支撑线
mp.plot(dates,support_line,c='limegreen',linewidth=3,label='Support')

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
