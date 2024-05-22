# mypackage/__init__.py

from .module1 import greet, display_numbers, reverse_word
from .module2 import greetting, pick_vowels

__all__ = ['greet', 'display_numbers', 'reverse_word', 'greeting', 'pick_vowels']


'''
    * `__all__`: this defines the public interface of the subpackage.
'''