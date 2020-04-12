from datetime import timedelta, datetime

import os

a1=timedelta(days=2,hours=6)
b1=timedelta(hours=4.6)
c1=a1+b1
print(c1)         #2 days, 10:36:00
print(c1.seconds)  # 38160
print(c1.seconds/3600)  # 10.6
print(c1.total_seconds()/3600) # 58.6


a2=datetime(2019,9,23)
print(a2+timedelta(days=10)) # 在原时间基础上加10天,但是不可以加月份
b2=datetime(2019,12,21)
d2=b2-a2  # 两个时间只差
print(d2.days)

Now=datetime.today()
print(Now)
print(Now.weekday()) #Return day of the week, where Monday == 0 ... Sunday == 6

from dateutil.relativedelta import  relativedelta
d3=Now+relativedelta(months=2,days=25)   #加月份和天数
print(d3)

'''
生成一个时间序列
'''

def range_date(start,stop,step):
    while start<stop:
        yield start
        start+=step
for d in range_date(datetime(2020,2,22),datetime(2020,3,2),timedelta(hours=6)):
    pass
    # print(d)


'''
字符串转换为日期
'''

from datetime import datetime
text='2019-09-20'
Y=datetime.strptime(text,'%Y-%m-%d')
print(Y) #2019-09-20 00:00:00
Z=datetime.now()
diff=Z-Y
print(diff) #205 days, 17:24:56.248533

nice_z=datetime.strftime(Z,'%A %B %d,%Y')
print(nice_z) #Sunday April 12,2020

'''
时区
'''
import pytz
import datetime

# UTC与SH时差8小时
print(pytz.all_timezones)
print(datetime.datetime.now())
tzone=pytz.timezone('UTC')
print(datetime.datetime.now(tzone))

