#Write a function:
#safe_call(func, a, b)
#that attempts to call the function func with the given arguments.
#The function must return a tuple of three elements:
#- a boolean indicating whether the call was successful,
#- the result of the function call (or None if an error occurred),
#- the name of the exception as a string (or None if no error occurred).
#If the function call raises one of the following exceptions:
#- ZeroDivisionError
#- TypeError
#- ValueError
#- IndexError
#- KeyError
#the function must not crash, but instead return information about the error.
#Any other exception types should not be handled.

def safe_call(func, a, b):
    try:
        result = func(a,b)
        return (True, result, None)
    
    except (ZeroDivisionError, TypeError, ValueError, IndexError, KeyError) as error:
        return (False, None, type(error).__name__)
    
    
def add(x,y):
    return x + y

safe_call(add, 4 ,5)
print(safe_call(add, 4, 5))
#(True, 9, None)
safe_call(add, 6 , "six seven")
print(safe_call(add, 6 ,"six seven"))
#(False, None, 'TypeError')
   
