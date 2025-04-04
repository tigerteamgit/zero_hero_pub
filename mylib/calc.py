"""
A calculator module

"""

def add(x, y):
    """Add two numbers"""
    return x + y

def sub(x, y):
    """Subtract two numbers"""
    return x - y

def mul(x, y):
    """Multiply two numbers"""
    return x * y

def div(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

#build a function to calculate the power of a number with a as the base and b as the exponent

def pow(a, b):
    """Calculate the power of a number"""
    return a ** b


