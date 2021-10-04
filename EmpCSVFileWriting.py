import csv
"""
#header = list(('EmpID','EmpName','Gender','Salary'))

#header = list(['EmpID','EmpName','Gender','Salary'])
header = ['EmpID','EmpName','Gender','Salary']
#empf=open(<<filename>>,<<mode>>)

#with open('employee.csv','w',newline="") as empf:

with open('employee1.csv','w',newline="") as empf:
#with open('employee1.csv','w') as empf:

    wrt = csv.writer(empf)  #writer obj
    count=0

    wrt.writerow(header)

    while(True):
        empid=int(input("Enter the employee ID"))
        empname=input("Enter the employee Name")
        gender=input("Enter the employee Gender")
        salary=eval(input("Enter the employee Salary"))  #int float...
        wrt.writerow([empid,empname,gender,salary])  #writerow(list(empid,empname,gender,salary))
        count+=1
        choice=input("Do you want add more record [Yes/No]")
        if choice.lower()=="no":
            break
    print("Employee data are written to CSV file with ",count," records")


"""
f1=open('employee1.csv')
csvr=csv.reader(f1)
print(type(csvr))  #collection
data=list(csvr)  # list of list
#table - rows and cols...

print(type(data))  #list for row of list for cols - list(row) of list(4)...
print(data)
for lines in data:
    for i in lines:
        #print(i)
        print(i,end="\t")
    print()
f1.close()

