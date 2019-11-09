#!/usr/bin/python3

import hypercomplex
import math
import random

from hypercomplex import Construction

LOOPS = 5
PRECISION = 10 ** -9

def random_vector ():
    return Construction((random.random(), random.random()))

o = Construction((1,0));
i = Construction((0,1));

print ("\nMultiplication Table tests...\n")
print ("Verify 1×1 = 1:")
if abs(o*o - o) <= PRECISION:
    print ("Success")
else:
    print ("Fail")
    exit()

print ("Verify 1×i = i:")
if abs(o*i - i) <= PRECISION:
    print ("Success")
else:
    print ("Fail")
    exit()

print ("Verify i×1 = i:")
if abs(i*o - i) <= PRECISION:
    print ("Success")
else:
    print ("Fail")
    exit()

print ("Verify i×i = -1:")
if abs(i*i + 1) <= PRECISION:
    print ("Success")
else:
    print ("Fail")
    exit()

print ("\nCummutative Product tests...\n")

for n in range(LOOPS):
    x = random_vector()
    y = random_vector()
    print ('check x × y = y × x')
    print ('check %s × %s = %s × %s' % (x, y, y, x))
    print ('result %s = %s' % (x*y, y*x))
    if abs(x*y - y*x) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

print ("\nWeak Alternative Condition tests...\n")

for n in range(LOOPS):
    x = random_vector()
    y = random_vector()
    print ('check (x × x) × y = x × (x × y)')
    if abs((x*x)*y - x*(x*y)) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    print ('check (x × y) × y = x × (y × y)')
    if abs((x*y)*y - x*(y*y)) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    print ('check %s × %s = %s × %s' % (x, y, y, x))
    print ('result %s = %s' % (x*y, y*x))
    if abs(x*y - y*x) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

print ("\nBrahmagupta–Fibonacci / Diophantus identity test..\n")
for n in range(LOOPS):
    x = random_vector()
    y = random_vector()
    print ('check (x × x) × y = x × (x × y)')
    if abs(x) * abs(y) - abs(x*y) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

print ("\nMoufang condition tests\n")
for n in range(LOOPS):
    x = random_vector()
    y = random_vector()
    z = random_vector()
    print ('x = %s\ny = %s\nz = %s' % (x,y,z))
    a = z*(x*(z*y))
    b = ((z*x)*z)*y
    print ('z × (x × (z × y)) = ((z × x) × z) × y ...')
    print ('%s = %s' % (a,b))
    if abs(a - b) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    c = x*(z*(y*z))
    d = ((x*z)*y)*z
    print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
    print ('%s = %s' % (c,d))
    if abs(c - d) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    e = (z*x)*(y*z)
    f = (z*(x*y))*z
    print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
    print ('%s = %s' % (e,f))
    if abs(e - f) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    g = (z*x)*(y*z)
    h = z*((x*y)*z)
    print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
    print ('%s = %s' % (g,h))
    if abs(g - h) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

print ("\nPower Associative tests\n")
for n in range(LOOPS):
    x = random_vector().normalize()
    y = random_vector().normalize()
    z = x * y
    print ('x = %s\ny = %s\nz = %s' % (x,y,z))
    print ('norm x = %s' % (abs(x)))
    if abs(x) - 1 <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    print ('norm y = %s' % (abs(y)))
    if abs(y) - 1 <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

    print ('norm z = %s' % (abs(z)))
    if abs(z) - 1 <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

print ("\nComplex Multiplication tests\n")
for n in range(LOOPS):
    x = random_vector()
    y = random_vector()
    a = x.a
    b = x.b
    c = y.a
    d = y.b
    m = Construction((a*c + x.isquare * d*b, d*a + b*c))
    z = x * y

    print ('x × y = (a,b) × (c,d) = (ac-db,da+bc)')
    print ('a = %s\nb = %s\nc = %s\nd = %s' % (a, b, c, d))
    print ('(ac-db,da+bc) = %s' % (m))
    print ('        x × y = %s' % (z))
    if abs(z - m) <= PRECISION:
        print ("Success")
    else:
        print ("Fail")
        exit()

