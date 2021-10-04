class Human:
    def talk(self):
        print('Inside humans talk method')
    def walk(self):
        print('Inside humans walk method')

class Employee(Human):
    def work(self):
        print('Inside employee work method')
    def walk(self):
        print('Inside employee walk method')       

class Painter(Employee):
    def walk1(self):
        print('Inside painter walk method')

e1=Employee()
e1.work()
e1.walk()
e1.talk()
e1.walk1()
