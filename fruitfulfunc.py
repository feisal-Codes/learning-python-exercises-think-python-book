import math

def compare(x,y):
    if x > y:
        return 1
    if x==y:
        return 0
    if x < y:
        return -1

def hypotenuse(a,b):

    c= math.sqrt(math.pow(a,2)+ math.pow(b,2)) 
    return c
def is_between(x,y,z):
    if x < y < z:
        print(True)
        return True
    else:
        print(False)
        return False
#is_between(2,2,2)
#recommended books
#Introduction to the Theory of Computation.

def factorial(n):
    if n==0:
        return 1
    else:
        print(n)
        recurse=factorial(n-1)
        result=n * recurse
        print(result)
        return result
factorial(3)


























