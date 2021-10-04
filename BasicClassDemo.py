'''
class Human:
    def walk(self):
        print('inside Humans walks method')

    def display(self):
        print('inside Humans display method')
print('this is first line')
obj1=Human()
obj1.walk()
obj1.display()
'''

class Human:
    #def __init__(self,sname,saddr):
       #print('invoking parents constructor method')
       # self.name=sname
       # self.addr=saddr


    def walk(self):
        print('inside Humans walks method')

    def display(self):
        print('inside Humans display method')
        print('student name is : %s' %(self.name))
        print('student address is : %s' %(self.addr))

    def __init__(self,sname,saddr):
        print('invoking parents constructor method')
        self.name=sname
        self.addr=saddr

print('this is first line')
obj1=Human('soumya','dkl')
obj2=Human('pinku','dkl')
obj1.walk()
obj1.display()
obj2.display()
