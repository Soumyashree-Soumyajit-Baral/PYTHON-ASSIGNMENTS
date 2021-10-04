l1=[12,23,45,69,82,47,32,10,46,44,8,102]
l2=list(filter(lambda a: not a%2,l1))
l3=filter(lambda a: a%2,l1)
l4=list(filter(lambda a: not a%5,l1))

print(l1,type(l1))
print(l2,type(l2))
print(l3,type(l3))
print(l4,type(l4))
        
