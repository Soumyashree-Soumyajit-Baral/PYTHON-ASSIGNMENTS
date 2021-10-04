from datetime import date

d1=date(2019,2,28)
#d1=date(year=2019,month=2,day=28)
d2=date.today()
print(d1)
print(d2)
print(d2.year)

#time class
from datetime import time
from datetime import datetime
t1=time(22,20,20)  # all parameters are optional.tz,fold...
t2=time(hour=22,minute=20,second=20)
t3=datetime.now().time()
t4=time()
print(t3, type(t3))

print(t1)
print(t2)
print(t2.hour)
print(t3)
print(t4)

