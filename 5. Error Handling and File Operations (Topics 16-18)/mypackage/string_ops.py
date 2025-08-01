
"""String operations module"""

def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def capitalize_words(s):
    """Capitalize all words in a string"""
    return ' '.join(word.capitalize() for word in s.split())

def count_vowels(s):
    """Count vowels in a string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
