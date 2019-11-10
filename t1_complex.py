#!/usr/bin/python3
#
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     reference: https://en.wikipedia.org/wiki/Complex_number
#

import math

from hypercomplex import Construction
from random       import random


LOOPS     = 20
PRECISION = 10 ** -9


# generate a random complex number ...
#
def random_vector ():
    return Construction((random(), random()))



print ("\nMultiplication Table tests...\n")

x = Construction((1,0,0,0))
i = Construction((0,1,0,0))

timestable = [
    ['1*1 =  1', x*x,  x],
    ['1*i =  i', x*i,  i],
    ['i*1 =  i', i*x,  i],
    ['i*i = -1', i*i, -x],
]

for entry in timestable:
    title, calc, expect = entry[::]

    print ("Verify %s:" % (title))
    print ("  expect: ", expect)
    print ("    calc: ", calc)
    print ("    diff: ", calc - expect)

    if calc == expect:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nCommutative Product tests...\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check x × y = y × x')
    print ('check %s × %s = %s × %s' % (x, y, y, x))
    print ('result %s = %s' % (x*y, y*x))

    if x*y == y*x:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nWeak Alternative Condition tests...\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check (x × x) × y = x × (x × y)')

    if (x*x)*y == x*(x*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (x × y) × y = x × (y × y)')

    if (x*y)*y == x*(y*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check %s × %s = %s × %s' % (x, y, y, x))
    print ('result %s = %s' % (x*y, y*x))

    if x*y == y*x:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nBrahmagupta–Fibonacci / Diophantus identity test..\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check (x × x) × y = x × (x × y)')

    if abs(x) * abs(y) - abs(x*y) <= PRECISION:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

print ("\nMoufang Loop Identity tests\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()
    z = random_vector()

    print ('x = %s\ny = %s\nz = %s' % (x,y,z))

    a = z*(x*(z*y))
    b = ((z*x)*z)*y

    print ('z × (x × (z × y)) = ((z × x) × z) × y ...')
    print ('z × (x × (z × y)) = %s' % (a))
    print ('((z × x) × z) × y = %s' % (b))

    if a == b:
        print ("Success\n")
    else:
        print ("    diff: ", abs(a - b))
        print ("Fail\n")
        exit()

    c = x*(z*(y*z))
    d = ((x*z)*y)*z

    print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
    print ('x × (z × (y × z)) = ', c)
    print ('((x × z) × y) × z = ', d)

    if c == d:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    e = (z*x)*(y*z)
    f = (z*(x*y))*z

    print ('check (z × x) × (y × z) = (z × (x × y) × z ...')
    print ('(z × x) × (y × z) = ', e)
    print ('(z × (x × y)) × z = ', f)

    e = (z*x)*(y*z)
    f = (z*(x*y))*z

    print ('check (z × x) × (y × z) = (z × (x × y) × z ...')
    print ('(z × x) × (y × z) = ', e)
    print ('(z × (x × y)) × z = ', f)

    if e == f:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    g = (z*x)*(y*z)
    h = z*((x*y)*z)

    print ('check (z × x) × (y × z) = z × ((x × y) × z) ...')
    print ('(z × x) × (y × z) = ', g)
    print ('z × ((x × y) × z) = ', h)

    if g == h:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nPower Associative tests\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector().normalize()
    y = random_vector().normalize()
    z = x * y

    print ('x = %s\ny = %s\nz = %s' % (x,y,z))
    print ('norm x = %s' % (abs(x)))

    if abs(x) - 1 <= PRECISION:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('norm y = %s' % (abs(y)))

    if abs(y) - 1 <= PRECISION:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('norm z = %s' % (abs(z)))

    if abs(z) - 1 <= PRECISION:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nComplex Multiplication tests\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    a = x.a
    b = x.b
    c = y.a
    d = y.b

    z = x * y
    m = Construction((a*c + x.isquare * d*b, d*a + b*c))

    print ('x × y = (a,b) × (c,d) = (ac-db,da+bc)')
    print ('a = %s\nb = %s\nc = %s\nd = %s' % (a, b, c, d))
    print ('(ac-db,da+bc) = %s' % (m))
    print ('        x × y = %s' % (z))

    if z == m:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()
