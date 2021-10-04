choice='y' 
while choice.lower()=='y' or choice.lower()=='yes':
    s=input('Enter your string').strip()
    print('No. of charecter in the given string :',len(s.strip()))
    n=input('Enter your word or letter').strip()
    if s.find(n)!=(-1):
        print('The word or letter exist in the given string')
        print('The no. of occurance is :',s.count(n))
        print('The index of first occurance is :',s.find(n))
        if s.count(n)>=2:
            print('The index of second occurance is :',s.find(n,s.find(n)+1))
    else:
        print('The word or letter is not exist in the given string')
    choice=input('Do you want to continue???')
