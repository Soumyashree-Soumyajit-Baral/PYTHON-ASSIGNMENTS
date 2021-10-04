try:
    print("Outer Try block")
    #print("Exception",10/0)
    #print("Exception")   
    try:
        print("Inner Try block")
        #print("Exception",10/5)   #part of both inner and Outer try
        #print("Exception",10+a1)
    except (NameError) as e:
        print("Inner except block")
        print("Exception",10/0)
    except (ZeroDivisionError,ValueError) as e:
        print("Inner 2nd except block")
        #print("Exception",10/0)
    else:
        print('there is no exceptions in try block')
        #print("Exception",10/0)
    finally:
        #print("Exception",10/0)
        print("Inner finally block")
        #print("Exception",10/0)
    print("Line after Inner",10/a1)
    
except (ZeroDivisionError,ValueError) as e:
    print("OuterException first line")
    #print("Outer Except block",a)

finally:
    print("Outer Finally block")

print("Line after Outer")

#1 normal flow with no exception

#2 exception raised in outer try statement and correspondng outer
#except block matched - Inner except and finally block wont be
#invoked for outer try exception,
#Outer except and finally wll be executed

#3 exception raised in outer try statement and correspondng outer
#except block not matched - results in abnormal termination

#4 exception raised in Inner try statement and correspondng inner
#except block matched - Inner except , finally , Outer finally exe

#5 exception raised in Inner try statement and correspondng inner
#except block not matched but outer except matched -
#Both Inner and Outer finally and outer except block will be executed.

#6 exception raised in Inner try statement and no inner and Outer inner
#except block not matched - only finally of both Inner and Outer
# will be executed and abnormal termination

#7 exception raised in inner except block itself and handled
# in outer except block - control
# will go to outer except block after exe inner finally block,
# finally block, and normal execution

#7A - try this scenario as well......
# even we can try another matching inner except block, but still
#control will go to outer except block only..

#8 exception raised in inner except block itself and not handled
# in outer except block - control
# will go to outer except block after exe inner finally block
# finally block, and abnormal execution

#9 exception raised in inner finally block itself and handled
# in outer except block - control will go to outer except block,
# outer finally block, and normal execution
#9A - Inner Finally (with or without Exception)

#10 exception raised in inner finally block itself and not handled
# in outer except block - control will go to
# outer finally block, and abnormal execution

#11 exception raised in normal statement of Outer block which
#is after inner finally block -control will go to outer except block ,if
#handled then normal if not then abnormal execution.

#12 exception raised in outer except block itself - abnormal 
#13 exception raised in outer finally block itself - abnormal
#14 exception in last line..- abnormal 
