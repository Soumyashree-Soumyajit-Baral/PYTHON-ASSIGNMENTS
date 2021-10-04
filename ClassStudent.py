class student:
    
    def __init__(self,sname,sid,sm1,sm2,sm3):
        self.name=sname
        self.id=sid
        self.mark1=sm1
        self.mark2=sm2
        self.mark3=sm3

    def display(self):
        
        print(f'Name of the student is {self.name}')
        print('ID of the student is %s' %self.id)
        print('Mark sequired in 1st subject is {}'.format(self.mark1))
        print('Mark sequired in 2nd subject is {}'.format(self.mark2))
        print('Mark sequired in 3rd subject is {}'.format(self.mark3))
        self.calc_tot()
        print('Total Mark :',self.tot)
        self.calc_avg()
        print('Average :',self.avg)
        self.calc_grade()
        print('Grade :',self.grade)
        self.calc_status()
        print('Status :',self.status)
        
    def calc_tot(self):
        self.tot=self.mark1+self.mark2+self.mark3
    def calc_avg(self):
        self.avg=self.tot/3
    def calc_status(self):
        self.status='pass' if self.avg>=50 else 'fail'
    def calc_grade(self):
        self.grade=('A+' if self.avg>=90 else 'A' if 90>self.avg>=80 else 'B+' if 80>self.avg>=70 else 'B'
                    if 70>self.avg>=60 else 'C' if 60>self.avg>=50 else 'F')

notimes=int(input('Enter no. of iteration :'))
count=1
while count<=notimes:

    Name=input('Enter name of the student :')
    Id=input('Enter id of the student :')
    M1=int(input('Enter mark1 :'))
    M2=int(input('Enter mark2 :'))
    M3=int(input('Enter mark3 :'))

    s1=student(Name,Id,M1,M2,M3)
    s1.display()
    count+=1
        
