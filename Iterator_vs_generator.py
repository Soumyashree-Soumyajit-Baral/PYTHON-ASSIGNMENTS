#Iterable/loop thru it.......collections....
#for i in range(1,100000000000000000000000000)
 #   1,2,3,....................
#l1 of 10000000000000000000000000 no of elements...

#iterator... class....


#Iterable vs Iterator(2 special methods which can retrieve only one element at a time)
"""
__iter__()   #processs of converting iterable to Iterator.

__next__()   #returns one element at a time..

#Collections are Iterable - which can be looped(For)

l1=[10,20,30,50,20,60]
print(type(l1))
#l1it=l1.__iter__()  #or
l1it=iter(l1)
print(type(l1it))

print(l1it.__next__()) #10
print(next(l1it))  #20
print(l1it.__next__()) #30
print(l1it.__next__()) #50
print(l1it.__next__()) #20

print(l1it.__next__()) #60
print(l1it.__next__())  #error.........
#print(l1it.__next__())


#how to create Custom/User-defined Iterator
class PowTwo:
    def __init__(self, max=0):
        self.n = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration("N value exceeded max value")
        result = 2 ** self.n #1,2,4,8,16,32,64,128,,36,,,,,,,100
        self.n += 1
        return result

p2=PowTwo(10)# PowTwo()#PowTwo(max=50)
print(p2,type(p2))

while True:
    try:
        print(p2.n,p2.__next__(),": ",end="")# p2.__next__()
    except StopIteration as e:
        print()
        print(e)
        break
"""

#generator function
def PowTwoGen(max=0):
    n = 1
    while n <= max:
        yield 2 ** n
        #Yield keyword similar to return statement...u can have more than yield statement
        n += 1


for i in PowTwoGen(10):
    print(i)
 

