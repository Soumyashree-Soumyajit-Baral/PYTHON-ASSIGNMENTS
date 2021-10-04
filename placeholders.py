a,b,c,d=10,11,123455.5536777888,12
print('Normal the sum of values of a,b and c is :',a+b+c)

print('Complex The sum of values of' ,a, ',' , b,
      ', and', c , 'is :', a+b+c)
#for conversions   #important question
#%i and %d ......for integer literals only
#%i .....used in c programming....so to use the python program inside c programming ..
#%d .....used in java...so to use the python program inside java ..
#%f .....for float literals only
#%s ......for anytype(float,int,bool)

print('value of %f is :%s'%(a,a))     #for single variable ,,you need not to keep it in ().
print('p The sum of values of %i , %d and %f is :%s' %(a,b,c,a+b+c))
print('p The sum of values of %i , %d and %10.4f is :%s' %(a,b,c,a+b+c))   #10.4 means total charecter should be 10 including '.' and 4 means 4 places after decimal points
print('p The sum of values of %f , %d and %i is :%d' %(a,b,c,a+b+c))

#place holders
#BP--blank placeholder
#NP--number place holder
#VP--variable place holder.....it was widely used

print('BPsum of variables {}, {} and {} is {}'.format(a,b,c,a+b+c))
print('BPsum of variables {}, {} and {} is {}'.format(a,float(b),c,a+b+c))

print('NPsum of the variables {0} , {1} and {2} is {3}'.format(a,b,c,a+b+c))
print('NPsum of the variables {2} , {3} and {1} is {0}'.format(a+b+c,c,a,b))

print('VPsum of the variables {a1} , {b1} and {c1} is {ee}'.format(a1=a,b1=b,c1=c,ee=a+b+c))
print('VPsum of the variables {a1} , {b1} and {c1} is {ee}'.format(c1=c,a1=a,ee=a+b+c,b1=b))

#f string (f or F)......to avoid place holders
print(f'the sum of values of {a} , {b} and {c} is : {a+b+c}')
print(F'Normal sum of values of {a} , {b} and {c} is : {a+b+c}') #similar to first print line

