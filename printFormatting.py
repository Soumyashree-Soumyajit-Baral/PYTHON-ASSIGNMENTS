a,b,c,d=10,11,123455.5536777888,12
print('Normal the sum of values of a,b and c is :',a+b+c)

print('Complex The sum of values of' ,a, ',' , b,
      ', and', c , 'is :', a+b+c)
# conversions take place   #important question
#%i and %d ......for integer literals only
#%i .....used in c programming....so to use the python program inside c programming ..
#%d .....used in java...so to use the python program inside java ..
#%f .....for float literals only
#%s ......for string and anytype(float,int,bool or any object(collection object also))

#Placeholder formatting.......when i want  some conversion to take place.........in realtime it is widely used,,preferable
#P--placeholder
print('value of %f is :'%a)     #for single variable ,,you need not to keep it in ().
print('P The sum of values of %i , %d and %f is :%s' %(a,b,c,a+b+c))       #%f will take 6 digit after dot bydefault   #flooring and ceilling takes place automatically
print('P The sum of values of %i , %d and %10.4f is :%s' %(a,b,c,a+b+c))   #10.4 means total charecter should be 10 including '.' and 4 means 4 places after decimal points
print('P The sum of values of %f , %d and %i is :%d' %(a,b,c,a+b+c))                       #if 8.4 there will be no space,,,,so the no. should be equal or less than total charecter
print('P The sum of values of %s , %s and %s is :%s' %(a,b,c,a+b+c))
#place holders   ......conversion doesnot take place
#BP--blank placeholder
#NP--number place holder
#VP--variable place holder.....it was widely used,,,,,,if i dont want any auto conversion and dont want to maintain the order
print('BPsum of variables {}, {} and {} is {}'.format(a,b,c,a+b+c))
print('BPsum of variables {}, {} and {} is {}'.format(a,float(b),c,a+b+c))   # here we can use conversion like float inside format method

print('NPsum of the variables {0} , {1} and {2} is {3}'.format(a,b,c,a+b+c))   #here the order is not importantbut indexing matters in order as compare to BP..according to order you can put the index
print('NPsum of the variables {2} , {3} and {1} is {0}'.format(a+b+c,c,a,b))

print('VPsum of the variables {a1} , {b1} and {c1} is {ee}'.format(a1=a,b1=b,c1=c,ee=a+b+c))  #order is not important and indexing dorsnot matter in order
print('VPsum of the variables {a1} , {b1} and {c1} is {ee}'.format(c1=c,a1=a,ee=a+b+c,b1=b))   #need not to maintain order

#f string (f or F-format),,,,,it is the new way,,,,,came to replace the placeholders as these are very lenthy ,,,,,here no conversion takes place,,,,,we can use it in realtime,,,python 3.6 onwards
print(f'the sum of values of {a} , {b} and {c} is : {a+b+c}')
print(F'Normal sum of values of {a} , {float(b)} and {c} is : {a+b+c}') #similar to first print line



print('%10.2f' %a)
print('%3.9f' %a)
print('%d' %c,end='$')
print('conclusion')
