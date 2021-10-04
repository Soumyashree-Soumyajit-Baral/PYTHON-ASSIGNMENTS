'''
sum=0
b=input('Enter numbers :').split()           #10 10
print(type(b),b)
for i in b:
    sum+=eval(i)
print('sum of all numbers :',sum)            #.......20
#sum=0                                      #if we will not initialize the variable,,,it will continue with the previous value and here the sum will be 220+10+10=40
a=input('Enter 2 numbers:').split()          #10 10
for j in a:
    sum+=eval(i)
print('sum value is :',sum)                 #40
c=eval(a[0])/eval(a[1])
print('devide value is :',c)

    


a=input('Enter 2 numbers :').split()
c=bin(int(int(a[0])/int(a[1])))      #only int data can be converted into bin ...so we have to use int function before converting binary.
print(c)                              #bin(int(float))
'''
#or

a=input('Enter 2 numbers :').split()
c=bin(int(eval(a[0])/eval(a[1])))
print(c)

