def zero(value = None):
    return 0 if value == None else value(0)
 
def one(value = None): 
    return 1 if value == None else value(1)   
def two(value = None): 
    return 2 if value == None else value(2)
def three(value = None): 
    return 3 if value == None else value(3)
def four(value = None): 
    return 4 if value == None else value(4)
def five(value = None): 
    return 5 if value == None else value(5)
def six(value = None): 
    return 6 if value == None else value(6)
def seven(value = None): 
    return 7 if value == None else value(7)
def eight(value = None): 
    return 8 if value == None else value(8)
def nine(value = None): 
    return 9 if value == None else value(9)

def plus(op): #your code here
    return lambda x : x + op
def minus(op): #your code here
    return lambda x : x - op
def times(op): #your code here
    return lambda x : x * op
def divided_by(op): #your code here
    return lambda x : x // op
