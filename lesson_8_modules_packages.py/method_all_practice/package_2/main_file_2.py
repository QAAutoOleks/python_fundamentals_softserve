from method_all_practice.package_1 import *

second_file.SOME_VARIABLE_2

# first_file.py is not available
# because import is done through 
# <from method_all_practice.package_1 import *>
# and in __init__.py at package_1
# only __all__ = ['second_file']