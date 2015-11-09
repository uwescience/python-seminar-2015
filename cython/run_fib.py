# Much more concise!

import pyximport  # This is part of cython
pyximport.install()
from fib import fib # This finds the pyx file, compiles automatically!
print(fib(10))
