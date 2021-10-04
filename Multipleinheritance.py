class Parent1:
    def talk(self):
        print('Inside Parent1 talk method')
    def work(self):
        print('Inside Parent1 work method')

class Parent2:
    def work(self):
        print('Inside Parent2 work method')
    def cry(self):
        print('Inside Parent2 cry method')       

class Child1(Parent1,Parent2):
    def walk(self):
        print('Inside child1 walk method')


e1=Child1()
e1.work()
e1.walk()
e1.talk()
e1.cry()
