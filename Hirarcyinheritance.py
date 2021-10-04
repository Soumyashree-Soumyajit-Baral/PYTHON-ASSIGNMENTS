class Parent:
    def talk(self):
        print('Inside Parent talk method')
    def work(self):
        print('Inside Parent work method')

class Child1(Parent):
    def work(self):
        print('Inside Child1 work method')
    def cry(self):
        print('Inside Child1 cry method')       

class Child2(Parent):
    def walk(self):
        print('Inside child2 walk method')


e1=Child1()
e1=Child1()
e1.work()
e1.walk()
e1.talk()
e1.cry()
#incomplete
