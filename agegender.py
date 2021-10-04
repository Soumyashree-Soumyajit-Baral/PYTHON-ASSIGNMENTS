choice='y'
while choice.lower()=='yes' or choice.lower()=='y':
    age=int(input('Enter age'))
    gender=input('Enter gender(f/m)')
    if age>=65:
        if gender=='f':
            print('Hi grandmaaaaaaa')
        else:
            print('Hi grandpaaaaaaa')
    elif age>=30 and age<65:
        if gender=='f':
            print('Hi aunty')
        else:
            print('Hi uncle')
    elif age>=18 and age<30:
        if gender=='f':
            print('Hi sis')
        else:
            print('Hi bro')
    else:
        print('Hi kids')
    choice=input('Do you want to continue???')
#else:
  #  print('The end')
