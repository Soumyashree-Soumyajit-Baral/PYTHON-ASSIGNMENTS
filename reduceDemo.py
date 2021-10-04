from functools import reduce
l1=[100,20,30,4,5,True]
s=reduce(lambda a,b:a+b,l1)
s1=lambda a,b:a+b
print('sum of the list elements :',s)
greatest=reduce(lambda a,b: a if a>b else b,l1)
smallest=reduce(lambda a,b: a if a<b else b,l1)
print('greatest among the list :', greatest)
print('smallest among the list :', smallest)
sum=reduce(s1,l1)
print('sum of the list elements :',sum)
