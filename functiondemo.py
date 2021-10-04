'''
def add(a,b):
    result=a+b
    return result

def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

'''
from Devfunctiondemo import add,sub,mul,div
from Math import *

a1,b1=input('Enter 2 integer value for arithmatic operation').split()
a1=int(a1)
b1=int(b1)
#sum=add(a1,b1)
print('sum of 2 numbers {} and {} is {}'.format(a1,b1,add(a1,b1)))
print('sub of 2 numbers %d and %d is %d' %(a1,b1,sub(a1,b1)))
print('mul of 2 numbers %d and %d is %d' %(a1,b1,mul(a1,b1)))
print('div of 2 numbers %d and %d is %f' %(a1,b1,div(a1,b1)))


#ad,sb,ml,di=DF.add(a1,b1)
res=add(a1,b1)
#print(ad,sb,ml,di)
print(type(res),res)
