from method_all_practice.package_1 import *

# first_file.py is not available
# because import is done through 
# <from method_all_practice.package_1 import *>
# and in __init__.py at package_1
# only __all__ = ['second_file']

public_name # available all public names from __init__.py
# public name is not available if __all__ = ['second_file'] is written
# _some_hidden_variable - isn't available
