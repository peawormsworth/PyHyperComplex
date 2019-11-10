#!/usr/bin/python3

import hypercomplex
from hypercomplex import Construction
import random
from random import random
from math import pi as π

LOOPS = 1
ATTRIBUTES = [
    '__add__',     '__radd__',            '__rsub__',    '__sub__',       '__rmul__',    '__rtruediv__',
    '__truediv__', '__mul__',             '__abs__',     '__invert__',    '__pow__',     '__neg__',
    '__pos__',     '__iadd__',            '__isub__',    '__imul__',      '__idiv__',    '__eq__', 
    '__getitem__', '__getitem__',         '__repl__',    '__str__',       '__init__',    '__ne__',
    '__complex__', 'log',                 'conj',        'norm',          'normalize',   'geodesic_norm',
    'tensor',      'is_real',             'is_complex',  'is_quaternion', 'is_octonion', 'is_sedenion',
    'flat',        'is_trigintaduonions', 'a',           'b',             're',          'im'
]

def random_vector ():
    return Construction((random(), random()))

z = random_vector()

print ('Check %s attributes:' % (type(z).__name__))
for attribute in ATTRIBUTES:

    if hasattr(z, attribute):
        print (" %s.%s ->exists" % (type(z).__name__,attribute))
    else:
        print (" %s.%s ->no such method" % (type(z).__name__,attribute))
        print ("Fail\n")
        exit()

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    m = random() * 5;
    z = random_vector()

    print ("\nRight vs Left multiplication")

    if m*z == z*m:
        print ("Success\n")
    else:
        print ("Fail\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    m = random() * 5;
    z = random_vector()

    print ("\nRight vs Left addition")

    if m+z == z+m:
        print ("Success\n")
    else:
        print ("Fail\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    m = random() * 5;
    z = random_vector()

    print ("\nRight vs Left subtraction")

    if m+(-z) - (-z)+m:
        print ("Success\n")
    else:
        print ("Fail\n")

print ("\nType match tests")
    
# todo: construct these randomly and loop ...
for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    types = [
        ['complex',    Construction((random(),random()))],
        ['quaternion', Construction((random(),random(),random(),random()))],
        ['octonion',   Construction((random(),random(),random(),random(),random(),random(),random(),random()))],
        ['sedenion',   Construction((random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random(),random()))]
    ]

    for entry in types:
        title, z = entry[::]
        print ("\ncheck z is %s...\n" % title)
        print ("z is complex:    ", z.is_complex())
        print ("z is quaternion: ", z.is_quaternion())
        print ("z is otonion:    ", z.is_octonion())
        print ("z is sedenion:   ", z.is_sedenion())



print ("\nPower and Log tests ...\n")


print ("\nlog(z) : ", z.log())
print ("SKIP: no valid tests or pre-determined solutions.")

print ("\nz^π : ", z ** π)
print ("SKIP: no valid tests or pre-determined solutions.")


