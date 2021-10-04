import pickle
#from pickle import *
from DevEmployeeClass import Employee
"""
e1=Employee(1001,"Janani",1000,9)
e2=Employee(1002,"Priya", 100,8)
e3=Employee(1003, 'Athaulla',500,10)

f1 = open("PickleEmployee2.txt",'wb')

pickle.dump(e1,f1)
pickle.dump(e2,f1)
pickle.dump(e3,f1)

f1.close()

"""

f1=open("PickleEmployee2.txt",'rb')
#e1 = pickle.load(f1)

while(True):
    try:
        e1 = pickle.load(f1)   #read one obj. at a time.....
        print(e1)
    except EOFError as eof:
        print("Reached End of the file", eof)
        break
    except Exception as e:
        print(e)
        break
f1.close()
print("Congratualtions  , u have read all EMP Objects")

