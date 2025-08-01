
"""A sample Python package"""

# Package-level imports
from .math_ops import add, multiply
from .string_ops import reverse_string, capitalize_words

# Package metadata
__version__ = "1.0.0"
__author__ = "Python Developer"

# What gets imported with "from mypackage import *"
__all__ = ['add', 'multiply', 'reverse_string', 'capitalize_words']

print(f"Initializing mypackage v{__version__}")
