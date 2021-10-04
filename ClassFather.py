class Father:
    def walk(self):
        print('Inside father walk method')

    def __init__(self,a,b):
        print('Inside father constructor method')
        self.a=a
        self.b=b

    def talk(self,a,b):
        print('Inside father talk method')
        
class son(Father):
    def cry(self):
        print('Inside cry method')

    def __init__(self,a,b,c,d):
        print('Inside child constructor method')
        #Father(a,b)
        super().__init__(a,b)
        self.c=c
        self.d=d

    def walk(self):
        super().walk()
        print('Inside child walk method')

f1=Father(10,20)
f1.walk()
f1.talk(10,20)
#f1.cry()#error
s1=son(10,20,30,40)
s1.walk()
s1.cry()
s1.talk(10,20)
