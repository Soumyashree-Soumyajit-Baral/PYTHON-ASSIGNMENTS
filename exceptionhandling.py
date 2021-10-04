from Selenium.MyException import *
#import selenium.MyException

try:
    a=int(input("Enter the 1st number"))
    b = int(input("Enter the second number >0 "))
    age=int(input('Enter the age'))
    if age<18:
        raise MyExceptionClass('you must 18 or above')
    c=a+b    
    print(a/b)



except MyExceptionClass as e:
    print(e)
except Exception as e:
    print("User u got Exception ",e.__class__,e)
else:
    print('there is no exception')
    
print('End of the Program')
    
#NameError, TypeError,ZeroDivision, ValueError
"""
except ZeroDivisionError as div:
    print("User u got zero division error",div)
except ValueError as ve:
    print("User u got Value error :",ve)
"""











#trigger zeroDivsion
    #if not age >=18:
    #    raise MyExceptionClass("Customer! You must be Adult to do Registration")


"""
try:   #keep in the watch list...
    #a = int(a)  #valueError
    #b = int(b)
    age=int(input("Enter your age"))

        #if not b:
    #    raise ZeroDivisionError("Ur Msg: Dividend cant be zero")
    #else:   
    #    result = a/b   #zero Division error

    if age < 18:    # requirement.. custom validation
        raise MyExceptionClass("U must be adult to run this program ")
    
    #db # file open.....

except(MyExceptionClass) as e:
    #print("Result is ", a/e1)
    print("Z Exception handled ", e)
    print("Exception",e.__class__, "Occured")


except(ZeroDivisionError,ValueError) as e:
    #print("Result is ", a/e1)
    print("Z Exception handled ", e)
    print("Exception",e.__class__, "Occured")

except(NameError) as e:
    try:
        print("Result is ",a/b) # this will raise ZDE if b value is 0
        print("N Exception handled ", e)
        print("Exception",e.__class__, "Occured")
    except Exception as e:
        print("Inner Try except block")
        print("Inner ZDE Exception handled ", e)
        print("Exception",e.__class__, "Occured")
    finally:
        print("Inner try Finally Block")

except Exception as e:
    print("Parent Exception handled ", e)
    print("Exception",e.__class__, "Occured")

else:
    print("Inside Else Block")
    
finally:
    #Close all your resource DB,File
    print("Inside Finally Block")

print("This is my normal line to be executed")




    #print(a+'Hello')

    #age=int(input("Enter your age"))
    
    #print(a/b)  #trigger zeroDivsion
    #if not age >=18:
    #    raise MyExceptionClass("Customer! You must be Adult to do Registration")



except Exception as e:
    print("V Exception handled ", e)
    print("Exception",e.__class__, "Occured")

    try:
        print (age)   #through anyother exception...
    except Exception as e:
        print("Exception",e.__class__, "Occured")
    finally:
        print("Inner Finally block")
else:
    print("Else block")
    
finally:
    print("Finally block")
    
print("This is my 1st last line of the prgram")
print("This is my 2nd last line of the prgram")

else:
    print("Else block")
finally:
    print("Finally block")

print("ths is my last line of the program")


except Exception as e:
    print("Base Exception handled ", e)
    print("Exception",e.__class__, "Occured")

    if not b >5:
        raise MyException("B must be greater than 5 ")
    
    #ValueError1= "Entered number is not > 5!"
    #raise ValueError("Entered number is not > 5!")
    
    print(sum11)
    print("Sum of 2 numbers %d and %d is %d" %(a,b,a+b))
    print("Subtract of 2 numbers %d and %d is %d" %(a,b,a-b))
    print("Multiply of 2 numbers %d and %d is %d" %(a,b,a*b))
    print("Divide of 2 numbers %d and %d is %f" %(a,b,a/b))
    print("End of the Program")
    #raise ValueError("Customized valueerror")
    
    #print(z)

    #raising the exception UserDefined Exception
    # we can raise predefined exception
    #ticket booking 18yrs old.. to do any transaction
    #coupon for discounts.... wrong coupon
    #min Quantity order  - 2 quantity...x # quantity
    #max 1 quantity - >1 -

except (MyException) as e:
   print("Base Exception handled ", e)
   print("Exception",e.__class__, "Occured")

except (ZeroDivisionError, ValueError) as e:
    print("V Exception handled ", e)
    print("Exception",e.__class__, "Occured")
except (Exception) as e:
    print("Base Exception handled ", e)
    print("Exception",e.__class__, "Occured")

else:
    print("Else block")
finally:
    print("Finally block")

print("Last line of the program")

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass
   
except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

try:
    a = int(input("Enter a + integer: "))
    if a <= 0:
        raise ValueError("That is not a + number!")
except ValueError as ve:
    print(ve)

#All possible combinations of try-except-else-finally block
#1. only try is invalid - (we need atleast except or finally)
#2. Must have try with except, try with finally
#3. try and else (w or w/o finally) alone wont work, we need except to have else
#4. one try with multiple excepts are allowed(only one else and finally)
    try(1)...except(n)....else(1)...finally(1)

    try(1)....finally(1)....except(1)..else(1)
#5. No common or comments statement in between try-except-else-finally block
#6. we can have nested try block...following above guidelines
#7.

try+except+finally+else....


#FileNotFoundError
NameError	Raised when a variable is not found in local or global scope.
EOFError	Raised when the input() function hits end-of-file condition.
ValueError	Raised when a function gets an argument of correct type but improper value
ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.
ImportError	Raised when the imported module is not found.
RuntimeError	Raised when an error does not fall under any other category.
KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
KeyError	Raised when a key is not found in a dictionary.
IndexError	Raised when the index of a sequence is out of range
AssertionError	Raised when an assert statement fails.
AttributeError	Raised when attribute assignment or reference fails.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raise when a generator's close() method is called.
MemoryError	Raised when an operation runs out of memory.
NotImplementedError	Raised by abstract methods.
OSError	Raised when system operation causes system related error.
OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	Raised when interpreter detects internal error.
SystemExit	Raised by sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
"""

