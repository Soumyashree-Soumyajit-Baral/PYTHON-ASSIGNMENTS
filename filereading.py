f1= open('typing.txt','r')
#print('cursor location',f1.tell())
#content=f1.read()
#print('cursor location',f1.tell())
#print('file contains:',content)
#content=f1.read(20)
#print('cursor location',f1.tell())
#print('file contains:',content)
tot=f1.read()
print('no of charecters',len(tot))
l=tot.split()
#print(type(tot))
print('no of words',len(l))

lines=tot.split('\n')
#print(lines)
print('no of lines',len(lines))
l1=[]
for i in l:
    if l.count(i)>=2:
        
        print('duplicate word is :', (i))
        print('no of occurance of duplicate word is :',l.count(i))

f1.seek(10)
print('cursor location',f1.tell())


f1.close()
#for i in lines:
   # print('cursor location',f1.tell())
    #print(i)
