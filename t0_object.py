#!/usr/bin/python3

import hypercomplex
from hypercomplex import Construction
import random

LOOPS = 1
PRECISION = 10 ** -9
ATTRIBUTES = ['__add__','__radd__','__rsub__','__sub__','__rmul__','__rtruediv__','__truediv__','__mul__','__abs__','__invert__','__pow__','__neg__','__pos__','__iadd__','__isub__','__imul__','__idiv__','__eq__','__ne__','__complex__','log','conj','norm','normalize','geodesic_norm','tensor','is_real','is_complex','is_quaternion','is_octonion','is_sedenion','is_trigintaduonions','__getitem__','flat','__getitem__','__repl__','__str__','__init__','a','b','re','im']

def random_vector ():
    return Construction((random.random(), random.random()))

a = Construction((1,2))

for attribute in ATTRIBUTES:
    print ('Check attribute %s.%s():' % (type(a).__name__, attribute))
    if hasattr(a, attribute):
        print ("Exists")
    else:
        print ("Fail")

for n in range(LOOPS):
    m = random.random() * 5;
    z = random_vector()
    print ("Right vs Left multiplication")
    if abs(m*z - z*m) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")

for n in range(LOOPS):
    m = random.random() * 5;
    z = random_vector()
    print ("Right vs Left addition")
    if abs((m+z) - (z+m)) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")

for n in range(LOOPS):
    m = random.random() * 5;
    z = random_vector()
    print ("Right vs Left subtraction")
    if abs((m-z) - (-z+m)) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")


#print ("log(z) : ", z.log())



