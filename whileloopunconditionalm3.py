notimes=int(input('Enter no. of iteration: '))       # the notimes should be greater than count.
count=1                                              #count should be lower than notimes. # condition is pre checked.

#choice='y'                                            #count=0,,,,while count<=count:.....infinity
while count<=notimes:                                 #while notime:  or notimes==True:.....infinity
                                                       #count=1,,,,,while notimes==False:......0 times
#while notimes:
#while choice.lower()=='yes' or choice.lower()=='y':      #while choice=='y':
    n=input('Enter the name of the student: ')
    m1=int(input('Enter mark_1: '))
    m2=int(input('Enter mark_2: '))
    m3=int(input('Enter mark_3: '))
    tot=m1+m2+m3
    avg=tot/3
   # status=0
    if avg>=50:
        status='pass'
    else:
        status='fail'
   # grade='A+','A','B+','B','C','F'
    if avg>=90:
        grade='A+'
    elif avg>=80 and avg<90:
        grade='A'
    elif avg>=70 and avg<80:
        grade='B+'
    elif avg>=60 and avg<70:
        grade='B'
    elif avg>=50 and avg<60:
        grade='C'
    else:
        grade='F'
    print(f'total mark: {tot}, average :{avg}, grade: {grade}, status: {status}')
    #print('total mark: %i, average :%s, grade: %s, status: %s' %(tot,avg,grade,status))
    #print('total mark:',tot,'average:',avg,'grade:',grade,'status:',status,sep=' ')
    #print('total mark :',tot,'\naverage :',avg,'\ngrade :',grade,'\nstatus :',status)
    #choice=input('Do you want to continue (y/n)')
    count+=1
print('I am done')
