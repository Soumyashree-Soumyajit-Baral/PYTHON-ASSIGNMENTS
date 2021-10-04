from time import time,ctime,localtime
#import time

# time - Simple ,
#datetime - more features......

print("Time() alone :",time())
print("Time() using Ctime ",ctime(time()))
print("CTime () alone ",ctime())
lc=localtime()
print(lc)
print(lc.tm_year,lc.tm_mon,lc.tm_mday,lc.tm_hour,lc.tm_min,lc.tm_sec)
print(lc.tm_wday,lc.tm_yday,lc.tm_isdst,lc.tm_zone)
