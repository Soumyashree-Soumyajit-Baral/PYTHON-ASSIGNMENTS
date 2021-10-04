from sys import argv
print(type(argv), argv)
sum=0
for i in argv[1:]:
   sum+=eval(i)
print('sum of all command line argument are:',sum)
