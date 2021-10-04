#Monkey Patching in Python (Dynamic Behavior)
#monkey patch refers to dynamic (or run-time) modifications of a class or module.
#Monkey patching is a technique used to dynamically update the behavior of a piece
#of code at run-time.

#It allows us to modify or extend the behavior of libraries, modules, classes or methods at
#runtime without actually modifying the source code
#Using this technique, we can actually change the behavior of code at run-time.
#decorators are applied at the time a function or class is defined,
#and monkey patching modifies an object at runtime
#monkey patching is useful if you know what you are doing and do not have the
#time to implement a SOLID solution. But you should never consider this a
#standard technique and build monkey patch upon monkey patch
#decorator #development time... ---- div(a,b),  smartdiv(a,b) --user calls div(a,b)
#monkey patching #runt timecaller.....call the pri

from functools import reduce

#l1=[10,20,30,40,50]
#sum=reduce(lambda a,b:a+b,l1)
#print(sum)

def display():
    print("Hi")

#User...
reduce=display   #Function aliasing....
reduce()    #it wll display not reduce.....

#from math import pi

import math #(pi=3.14444444)
print("Default PI Value ", math.pi)
math.pi=5   # monkey patching...
print("Default PI Value ", math.pi)
"""
#filter(),map(), reduce()

def div(a,b):
    print("Inside normal Div method")
    return a/b

def smartdiv(a,b):
    print("Inside Smart Div method")
    if not b:
        return 0
    else:
        return a/b   #div(a,b)

a=[int(x) for x in input("Enter 2 numbers").split()]  #a list of integer-2
print("Div fun reference ", id(div), "Smart Div Reference", id(smartdiv))

if a[1]>0:
    print("Div fun reference ", id(div))
    print("Sum of {} and {} value is {}".format(a[0],a[1],div(a[0],a[1])))
else:
    div=smartdiv    #monkey patching.....function aliazing.....
    print("Div fun reference ", id(div))
    print("Sum of {} and {} value is {}".format(a[0],a[1],div(a[0],a[1])))


        
def func1():
    print("Inside func1")

def func2():
    print("Inside func2")

func1()
print("Func1 ", id(func1))
print("Func2 ", id(func2))
func1=func2
print("Func1 ", id(func1))
print("Func2 ", id(func2))

func1()


class A: 
     def func(self): 
          print ("func() is being called")

def monkey_f(self): 
     print ("monkey_f() is being called") 
   
# replacing address of "func" with "monkey_f" 
A.func = monkey_f 
obj = A() 
  
# calling function "func" whose address got replaced 
# with function "monkey_f()" 
obj.func() 
"""
