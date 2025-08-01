
"""A simple math utilities module"""

# Module-level variables
PI = 3.14159
E = 2.71828

# Module-level functions
def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def circle_area(radius):
    """Calculate circle area"""
    return PI * radius ** 2

def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Code that runs when module is imported
print(f"Math utils module loaded! PI = {PI}")

# This runs only when script is executed directly
if __name__ == "__main__":
    print("Running math_utils as main program")
    print(f"Testing: 5! = {factorial(5)}")
