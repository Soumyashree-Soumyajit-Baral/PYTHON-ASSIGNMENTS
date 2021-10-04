'''
import datetime
class Employee:
    Empr_Name = 'ABC India limited'

    def calc_sal(a):
        #a.salary = a.rph*a.no_hours*30  #initialising instance variable
        #a.salary = a.rph*a.no_hours*a.daysinmonth()
        a.salary = a.rph*a.no_hours*Employee.daysinmonth()

    def display(a):
        a.Empr_Name = 'Empire of soumya'
        Employee.Empr_Name ='Reliance industry'
        print('Before by object name', a.Empr_Name)
        print('Before by object name', Employee.Empr_Name)
        #print(a.id)
        #print(a.name)
        a.calc_sal()
        print(a.salary)
        a.status='Married'
        #print(a.status)
        a.id=200001
        #print(a.id)
    def __init__(a,id1,b,c,d):
        #print('constructor',id(a))
        #print('inside python constructor method')
        a.id=id1
        a.name=b
        a.rph=c
        a.no_hours=d

    def delete(cls):
        print('Before deleting using self :', cls.salary)
        del cls
        #print('Before deleting using self :', self.salary)
        #del Employee

    @classmethod
    def demo1(cls):
        print('Instance memory ref',type(Employee),id(Employee))
        print('Instance memory ref',type(cls),id(cls))
        print(Employee.Empr_Name)
        print(cls.Empr_Nama)
        cls.delete()
        print(cls.Empr_Nama)
        
    @staticmethod
    def daysinmonth():
        print('Inside static method')
        today=datetime.datetime.now()
        month=int(today.strftime('%m'))
        year=int(today.strftime('%y'))
        print(year,month)
        normalmonths=[31,28,31,30,31,30,31,31,30,31,30,31]
        leapmonths=[31,29,31,30,31,30,31,31,30,31,30,31]
        isleap=not year%400
        if isleap:
            print('Leap year Days',leapmonths[month-1])
            return leapmonths[month-1]
        else:
            print('Normal year Days',normalmonths[month-1])
            return normalmonths[month-1]




print('program starts here')
e1=Employee(1001,'jaanvi',1000,9)
print('Through class name :', Employee.Empr_Name)
print('Through obj ref e1 :', e1.Empr_Name)
e1.display()
print(Employee.Empr_Name)
print(e1.Empr_Name)
'''
import DevEmployeeClass

e2=DevEmployeeClass.Employee(1002,'athaullasir',800,8)
#Employee.Empr_Name ='XYZ India limited'     #reassigning
#e2.Empr_Name = 'soumya empire'
#print('Through class name :', Employee.Empr_Name)
#print('Through obj ref e1 :', e2.Empr_Name)
#print(e2.id)
e2.display()
#print(e2.id)
#e2.id=2001
#print(e2.id)
#print('Through class name :', Employee.Empr_Name)
#print('Through obj ref e1 :', e2.Empr_Name)
#print('through obj ref e2 :', e2.Empr_Name)
#print('salary information', e2.salary)
#e2.delete()
#del e2.salary
#del e2
print('salary information', e2.salary)
#e2.display()
