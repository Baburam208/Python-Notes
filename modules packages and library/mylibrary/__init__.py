# mylibrary/__init__.py

### Description
"""
The `__init__.py` file initializes the 'mylibrary' package and 
defines what is availale at the top level of the library.
"""

from .math_utils.basic import square, multiply
from .math_utils.advanced import divide
from .string_utils.formatter import uppercase, lowercase
from .string_utils.validator import is_palindrome

__all__ = ['square', 'multiply', 'divide', 'uppercase', 'lowercase', 'is_palindrome']

"""
    * `__all__`: this defines the public interface of the package, specifying what 
    is available when `import *` is used.
"""

"""
NOTE: 
    Empty `__init__.py` file: If `__init__.py` files do not contain imports or definitions 
    of `__all__`, you cannot access the package's components directly through the package name.

EXPLICIT Imports:
    You can still access all functionality by importing the specific modules explicitly.
"""