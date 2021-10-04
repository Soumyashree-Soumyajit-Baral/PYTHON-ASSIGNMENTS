'''
def div(a,b):
    if not b:
        return 0
    if a<b:
        a,b=b,a
        return a/b
    else:
        return (a/b)
a=input('enter 2 nos for division').split()
print(type(a))
#b=int(input('enter second no for division'))
#res=div(int(a[0]),int(a[1]))
print('answer is :',div(int(a[0]),int(a[1])))





'''
def smartdiv(f):
    print('l1 inside decor func')
    print('address of f :',id(f))
    def inner(i,j):
        print('l4 inside inner of decor func')
        if not j:
            print('l5 j is zero, returning zero bydefault')
            return 0
        if i<j:
            i,j=j,i
            return i/j
        else:
            res=f(i,j)
            return res
    print('l2 address of inner :',id(inner))
    return inner
@smartdiv    #function alliasing takes place internaly,,,,,div=smartdiv(div)
def div(a,b):
    print('l5 inside original devide ',id(div))
    return a/b

a=input('enter 2 nos').split()
print('l3 first line of my main program')
print('inner id using div ',id(div))
oldres=div(int(a[0]),int(a[1]))
print('l6 old devide of {} and {} is {}'.format(a[0],a[1],oldres))
#f1=smartdiv(div)
#oldresult=f1(int(a[0]),int(a[1]))
#print('l6 old devide of {} and {} is {}'.format(a[0],a[1],oldresult))            

'''
def smartdiv(f):    #whats this argument?????
    print("L#1 Inside Decor Function")
    print("Address of f : ", id(f))o
    def inner(i,j):
        print("L#4 Inside Inner of Decor")
        if not j:   #number can be used condition >0 True 0 - False
            print("L#5 j is zero - Zero Divide error so returning zero default")
            #b=1
            #f(a,b)
            return 0
        else: #(a and b is normal...normal execution...
            #return i/j - 
            #print(id(f))
            #return i/j
            #avoid duplicate....
            res=f(i,j)   #actual div function
            return res
            #return f(i,j)
    print("L#2 Address of Inner : ", id(inner))
    return inner

#function aliasing   div=smartdiv(div)
@smartdiv # remove this and use decorfunc = smartdiv(div) to have both
def div(a,b):  #15lnes of code....
    print("L#5 Inside original Divide method",id(div))
    return a/b
a=input("Enter 2 numbers").split() #"10" "20"
#a=[int(x) for x in input("Enter 2 numbers").split()]   #list comprehensive
print("L#3 1st line of my main program")
print("inner ID using div ",id(div))   #id----inner.......
#f(10,20) , div(10,20).....
#result=div(a[0],a[1])  #normal div invoked indirectly
#print("L#6 Divide of {} and {} is {}".format(a[0],a[1],result))

oldresult=div(int(a[0]),int(a[1]))  #normal div invoked indirectly
print("L#6 OLD Divide of {} and {} is {}".format(int(a[0]),int(a[1]),oldresult))
'''
