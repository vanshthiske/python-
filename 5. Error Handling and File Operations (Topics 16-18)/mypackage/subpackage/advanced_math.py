
"""Advanced math operations"""

def power(base, exponent):
    """Calculate base raised to exponent"""
    return base ** exponent

def root(number, n=2):
    """Calculate nth root of a number"""
    return number ** (1/n)

def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
