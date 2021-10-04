import json

"""
emp_dict1={"EID":1001,"Ename":"Athaulla","Salary":120020.70,
           "BonusElig":True, "LTAElg":None}

emp_dict2={"EID":1002,"Ename":"Reena","Salary":104033.56,
           "BonusElig":True, "LTAElg":None}
emp_dict3={"EID":1003,"Ename":"Sunitha","Salary":98909.70,
           "BonusElig":False, "LTAElg":None}

#going to write Python (Dictionary) Obj to JSON File....

#f1 = open("TyuteeEmp.json",'w')

#json.dump([emp_dict1,emp_dict2,emp_dict3],f1)

#json.dump(emp_dict1,f1)
#json.dump(emp_dict2,f1)
#json.dump(emp_dict3,f1)
#f1.close()

json_str1=json.dumps(emp_dict1)
#,indent=5
print("Printing JSON Strng format")
print(type(json_str1))
print(json_str1)

"""
json_str1="""
{
 "eid":1001,
 "ename":"Athaulla",
 "married":true

}
"""
empdict1=json.loads(json_str1)

for i in empdict1:
    print("{}:{}".format(i,empdict1[i]))

"""
#connect to particular website......httprequest
#print("Printing Python Dict Object from JSON String")

#Python = int, float, Bool (True/False), String, Object, None
#JSON = number, bool (true/false), Object, null
#JSON Key shld be enclosed in double quotes...




#Reading JSON string from JSON File
with open("TyuteeEmp.json",'r') as f2:
    dictobj=json.load(f2) #Table format List of Dictionary..
    print()
    for i in dictobj:  
        for j in i:
            print("{}:{}".format(j,i[j]),end="\t")
        print()
#f2.close
#
#json.dump(emp_dict2,f1)
#json.dump(emp_dict3,f1)

with open("emp.json",'r') as f2:
    while(True):
        try:
            dictobj=json.load(f2)
            print(type(dictobj))
            for i in dictobj:
                print("{}:{}".format(i,dictobj[i]))
        except EOFError as e:
            print("Error Encountered", e)
            break
"""
