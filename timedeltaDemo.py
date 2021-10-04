from datetime import timedelta,date

fd = timedelta(days=-365,hours=6)
#CC cycledate..45days...payment date... 
#amazon - 1 year from now.....subscrption end date 2nd Sep 2022
#Library System - DOO+10days ...returnDate=12th Sep 2021
cd=date.today()
#pd = date(2021,12,24) #date.today()
print(fd)
print(cd)
print(cd+fd)   #2nd Sep 2021+365-----2nd sep 2022
"""

#fd = timedelta(days=0,seconds=0,microseconds=0,  ----
#milliseconds=0,minutes=0,hours=0,weeks=0)
#All args are optional and default to zero.
#Arguments may be integer or float and + or -

#Date comparison
#==, < , >, !=,>=, <= between date class and datetime class
d1 = date(2018,7,29)
d2= date(year=2020,month=6,day=30)
print("Is Same ", d1==d2)
print("Is greater ", d1>d2)
print("Is lesser ", d1<=d2)
d3=d1-d2
print(d3, type(d3))

#d5=d2*d1
#print(d5, type(d5))
#d6=d2/d1
#print(d6, type(d6))


dob=date(2000,4,30)
cdate=date.today()  #2021,6,1)
age=cdate.year - dob.year #---- 2021-2000 = 21 -1
print(age)
age=cdate.year-dob.year - ((cdate.month,cdate.day) < (dob.month,dob.day))
print(age)

#assignment age: year, months, days....
"""



