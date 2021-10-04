import datetime
import pytz
#import datetime.datetime


#date  - store date(year,month,day)
#time   - hours,mins,sec,milli, microsecs..
#datetime - year,month,day,hours,mins,sec,milli, microsecs
#timedelta - delta/difference between 2 dates....
#amazon subscriptions...25th Dec 2021+30 - 24th Jan 2022, subscriptionends


#from datetime import date
x = datetime.datetime.now(pytz.timezone('America/New_York'))  # returns current date and time, We can provide tz
x1= datetime.datetime.today() # default timezone
y = datetime.datetime(1980,5,17) #DOB  1985, 5th Jan
y1 = datetime.datetime(1980,5,17,20,20,20)
y2=datetime.datetime(year=1980,month=5,day=5,hour=13,minute=13)
z=datetime.datetime(year=2019,month=5,day=29,hour=15,minute=23,second=23)
print("X ", x)
print("x1 ",x1)
print("Y ",y)
print("Y1 ",y1)
print("Y2 ",y2)
print("z ",z)
print(x.year)

print("Weekday : ",x.strftime("%A"))
print("Offset :", x.strftime("%z"))
print("TimeZone :", x.strftime("%Z"))
print("Date :", x.strftime("%x"))
print("Time :", x.strftime("%X"))
#print(y)

#%a	Weekday, short version (wed)
#%A	Weekday, full version	(Wednesday)	
#%w	Weekday as a number 0-6, (0 is Sunday)		poiu
#%d	Day of month 01-31	
#%b	Month name, short version	(Dec)	
#%B	Month name, full version	(December)	
#%m	Month as a number 01-12	        	
#%y	Year, short version, without century	(20 for 2020)
#%Y	Year, full version	(2020)	
#%H	Hour 00-23		
#%I	Hour 00-12		
#%p	AM/PM	
#%M	Minute 00-59		
#%S	Second 00-59		
#%f	Microsecond 000000-999999		
#%z	UTC offset	+0100	
#%Z	Timezone	CST	
#%j	Day number of year 001-366		
#%U	Week number of year, Sunday as the first day of week, 00-53		
#%W	Week number of year, Monday as the first day of week, 00-53		
#%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%x	Local version of date	12/31/18	
#%X	Local version of time	17:41:00	

