'''
import random                    #from random import *...to avoid using random everywhere
r=range(30)
results=random.choices(r,k=20)   #results=choices(r,k=20)
l=list(results)
print(l)
s=set(l)
l1=list(s)
print(l1)
c=len(l)-len(l1)
c1=len(l)-c
print('The no. of duplicates are :',c)
print('The no. of unique numbers are :',c1)




from random import *
i=(randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15))
l=list(i)
print(l)
s=set(l)
l1=list(s)
print(l1)
c=len(l)-len(l1)
c1=len(l)-c
print('The no. of duplicates are :',c)
print('The no. of unique numbers are :',c1)
   

'''


from random import *
l=list()
for i in range(20):
    a=randint(0,30)
    l.append(a)
print(l)
l1=list()
for j in l:
    if j not in l1:
        l1.append(j)
print(l1)
c=len(l)-len(l1)
c1=len(l)-c
print('The no. of duplicates are :',c)
print('The no. of unique numbers are :',c1)










'''

from random import *
l=list()
for i in range(20):
    i=randint(0,30)
    l.append(i)
print(l)    
s=set(l)
l1=list(s)
print(l1)
c=len(l)-len(l1)
c1=len(l)-c
print('The no. of duplicates are :',c)
print('The no. of unique numbers are :',c1)









import random
r=range(50)
results=random.choices(r,k=20)
l=list(results)
for i in l.count(results):print(i)




'''
