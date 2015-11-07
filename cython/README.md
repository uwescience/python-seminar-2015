These materials are heavily based on an excellent scipy tutorial by Kurt Smith 
(Enthought). The videos for this tutorial are [here](https://www.youtube.com/watch?v=JKCjsRDffXo).

## Cython :

Writing code in python is easy: because it is dynamically typed, we don't have
to worry to much about declaring variable types (e.g. integers vs. floating
point numbers). Also, it is interpreted, rather than compiled. Taken together,
this means that we can avoid a lot of the boiler-plate that makes compiled,
statically typed languages hard to read. However, this incurs a major drawback:
performance for some operations can be quite slow.

Whenever possible, the numpy array representation is helpful in saving
time. But not all operations can be vectorized.

Cython is a technology that allows us to easily bridge between python, and the
underlying C representations. The main purpose of the library is to take code
that is written in python, and, provided some additional amount of (mostly
type) information, compile it to C, compile the C code, and bundle the C
objects into python extensions that can then be imported directly into python.

You can easily install cython from the command line:

    conda install cython

Head over to the notebook `001-cython` to see what this is all for.

We start with an example of the speedup you might get from a trivial addition
to your code, combined with a compilation step.

This is not the typical usage pattern of python/cython code. Let's consider how
to integrate this into a larger context.

## Compiling cython code

Typical usage of cython will include the writing of python and cython code side
by side. Consider our fibonacci series code. If we place it in a `.pyx` file,
we can then ask cython to compile this for us. We use the python `distutils`
library to do that. Let's take a look at `fib.pyx` and `setup_fib.py` to see
how it's done.

To compile the fib.pyx file, we run the `setup` file:  

        python setup_fib.py build_ext --inplace [--compiler=mingw32 #only for Windows!]


This creates a `fib.o` compiled object and a `fib.so` bundled python extension,
such that in a python/ipython session, you can now do:

    import fib
    a = fib.fib(10)

Note the error that comes out if you run the function with an input for which
int(foo) would fail. For example, we can try running:

	 fib.fib("a string")

The dynamically typed python could not identify that this is not the right type
for the operations in this function, but the C code, that is statically typed
recognizes this upfront.

### Using `pyximport`

An even easier way to use cython is through the pyximport mechanism (see run_fib.py)

In case you are wondering where the pyx file is in this case, it is under a
conventional location: ~/.pyxbld/

## Optimizing further: using `cdef`

Typically, we will write a cython module with functions, classes, and so
forth. Some of these objects need to have a public interface, so that they can
be used by our python code, but some of these are local to the cython module,
and don't need to be available to use in python code. We can gain additional
performance boosts by defining them in such a way that the compiler knows they
are  

We can use `cdef` to define local functions and even types. For example:

   cdef float distance(float *x, float *y, int n):
       cdef:  # same as using two lines each starting with `cdef`
           int i
	   float d = 0.0
	for i in range(n):
	    d += (x[i]- y[i]) **2
	return d

    cdef class Particle(object):
        cdef float psn[3], vel[3]
	cdef int id

These defined objects would be unavailable from the python side, but will be
available to other functions within that pyx file/module. They have the
advantage that they have no python overhead when called, so their performance
is very good.  
       
### Using `cpdef`

Alternatively, defining it with `cpdef` will create both the cython-available
and the python-available versions of the function. Not as simple, because the
inputs now need to be something that python knows how to produce (array
pointers are not one of those...). This gives you the advantage of 

   cpdef float distance(float[:] x, float[:] y):  # Defined as typed memory views
       cdef int i
       cdef int n = x.shape[0]
       cdef float d = 0.0
       for i in range(n):	
	    d += (x[i] - y[i]) ** 2
       return d

Finally, if you just want to define this in cython (or python, for that
matter), this also works (as long as you have an `import numpy as np`):

	 def distance(x, y):
	     return np.sum((x-y) **2)

### How do we know this helps: using annotations

Recally that cython compiles your code into C code for a python extension
module. Depending on the information you provided (type annotations,
`cdef`/`cpdef`) this will require more or less complicated C code. Cython
provides tools to explore and optimize this process. To create an annotation of
your file, on the command line run:

    cython -a file_name.py

This generates your `.c` file, but also an `html` file with information about the
line-by-line cost of the `pyx` file. The shade of yellow corresponds the number of
lines of c that were generated, which highly correlates with the time of
execution. 
	     
Here's how this would be used in practice. Consider a simple case in which a
helper function is used to calculate an increment, and this function is used by
a more general function (`increment1.pyx`):

	def increment(int num, int offset):
	    return num + offset

	def increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = increment(val, offset)
		result.append(res)
	    return result

Cythonize this file, and open the `increment1.html` file, which annotates the
cythonization process.

Now, let's consider how much better we would do using `cdef` (`increment2.pyx`):

	cdef int fast_increment(int num, int offset):
	    return num + offset

	def fast_increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = fast_increment(val, offset)
		result.append(res)
	    return result

Notice that in the second example, the lines corresponding to the first
function are now completely white. The second example will also be much faster,
because there is less python-related overhead in that one. Cython can compile
the fast_increment function without needing to do things like python type-checking, etc.
 
In this case, we may as well use cpdef:

	cpdef int increment_either(int num, int offset):
	    return num + offset
	def fast_increment_sequence(seq, offset):
	    result = []
	    for val in seq:
	        res = increment_either(val, offset)
		result.append(res)
	    return result

The function increment_either is only fast when called by
fast_increment_sequence. However, you can now independently call it from 
python (in which case, it will be slow).

## Compling c extensions from c code.

This is useful if you want to use legacy c code. Consider the toy example in
fact.pyx/fact.h. 

     cythonize fact.pyx  
    
     gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/arokem/anaconda3/include -arch x86_64 -I/Users/arokem/anaconda3/include/python3.4m -c fact.c

     gcc -bundle -undefined dynamic_lookup -L/Users/arokem/anaconda3/lib -arch x86_64 fact.o -L/Users/arokem/anaconda3/lib -o fact.so
    
Similar principles can be used with much more complex C code.

## Using `cimport`

Look at the sinc tutorial example, and `cimport clib.math`
