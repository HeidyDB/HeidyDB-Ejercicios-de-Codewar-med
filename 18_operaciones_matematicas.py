
def zero(op=None):
    if op:
        return op(0)
    return 0
def one(op=None): 
    if op:
        return op(1)
    return 1
    
def two(op=None): 
    if op:
        return op(2)
    return 2

def three(op=None):
    if op:
        return op(3)
    return 3

def four(op=None):
    if op:
        return op(4)
    return 4

def five(op=None):
    if op:
        return op(5)
    return 5

def six(op=None): 
    if op:
        return op(6)
    return 6

def seven(op=None): 
    if op:
        return op(7)
    return 7

def eight(op=None): 
    if op:
        return op(8)
    return 8

def nine(op=None): 
    if op:
        return op(9)
    return 9

def plus(n): 
    return lambda x : x+n  
def minus(n): 
    return lambda x : x - n
def times(n): 
    return lambda x : x * n
def divided_by(n): 
    return lambda x : x // n

print(seven(plus(five())))      # Imprime: 12
print(four(minus(two())))       # Imprime: 2