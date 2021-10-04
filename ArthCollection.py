l0=[13,43,34,55,66,26,68,75,70,90,88]
l1=[12,31,22,41,23,12,55,40,68,30,58]
l2={77,88,32,12,56,45,25,69,80}
l3=(90,60,30,120,150)

l3=list(map(lambda a: a+5,l1))
print(l3)
l5=set(map(lambda b: b-10,l2))
print(l5)
l6=tuple(map(lambda c: c*10,l3))
print(l6)
l7=list(map(lambda d: d/2,l1))
print(l7)
l8=list(map(lambda a,b: a+b,l0,l1))
print(l8)
l9=list(map(lambda b,c: b-c,l0,l1))
print(l9)
l10=list(map(lambda b,c: b*c,l0,l1))
print(l10)
l11=list(map(lambda b,c: b/c,l0,l1))
print(l11)
