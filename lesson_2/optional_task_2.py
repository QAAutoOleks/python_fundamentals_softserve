import importlib
import sys
import io

buffer = io.StringIO()
sys.stdout = buffer

this = importlib.import_module("this")
sys.stdout = sys.__stdout__

import codecs

python_philosophy_full = codecs.decode(this.s, 'rot_13')
python_philosophy = python_philosophy_full[34::]

better_count = python_philosophy.count('better')

never_count = python_philosophy.count('never')

is_count = python_philosophy.count('is')

zen_upper = python_philosophy.upper()

zen_replace = python_philosophy.replace('i', '&')
print(zen_replace)