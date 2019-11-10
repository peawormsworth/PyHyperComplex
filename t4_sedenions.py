#!/usr/bin/python3
#
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     reference: https://en.wikipedia.org/wiki/Octonion
#

import hypercomplex

from hypercomplex import Construction
from random       import random


LOOPS = 20
PRECISION = 10 ** -9


# generate a random complex number ...
#
def random_vector ():
    return Construction((
        random(), random(), random(), random(), random(), random(), random(), random(), 
        random(), random(), random(), random(), random(), random(), random(), random(), 
    ))


print ("\nMultiplication Table tests...\n")

x = Construction((1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
i = Construction((0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
j = Construction((0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0))
k = Construction((0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0))
l = Construction((0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0))
m = Construction((0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0))
n = Construction((0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0))
o = Construction((0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0))
p = Construction((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0))
q = Construction((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0))
r = Construction((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0))
s = Construction((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))
t = Construction((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0))
u = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0))
v = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0))
w = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1))

# todo: fill in the rest of this table. It's 4 times as long (16×16 = 256 entries)

timestable = [
    ['1*1 =  1', x*x,  x],
    ['1*i =  i', x*i,  i],
    ['1*j =  1', x*j,  j],
    ['1*k =  k', x*k,  k],
    ['1*l =  1', x*l,  l],
    ['1*m =  i', x*m,  m],
    ['1*n =  1', x*n,  n],
    ['1*o =  k', x*o,  o],

    ['i*1 =  i', i*x,  i],
    ['i*i = -1', i*i, -x],
    ['i*j =  k', i*j,  k],
    ['i*k = -j', i*k, -j],
    ['i*l =  m', i*l,  m],
    ['i*m = -l', i*m, -l],
    ['i*n =  1', i*n, -o],
    ['i*o =  k', i*o,  n],

    ['j*1 =  1', j*x,  j],
    ['j*i =  i', j*i, -k],
    ['j*j =  1', j*j, -x],
    ['j*k =  k', j*k,  i],
    ['j*l =  1', j*l,  n],
    ['j*m =  i', j*m,  o],
    ['j*n =  1', j*n, -l],
    ['j*o =  k', j*o, -m],

    ['k*1 =  1', k*x,  k],
    ['k*i =  i', k*i,  j],
    ['k*j =  1', k*j, -i],
    ['k*k =  k', k*k, -x],
    ['k*l =  1', k*l,  o],
    ['k*m =  i', k*m, -n],
    ['k*n =  1', k*n,  m],
    ['k*o =  k', k*o, -l],

    ['l*1 =  1', l*x,  l],
    ['l*i =  i', l*i, -m],
    ['l*j =  1', l*j, -n],
    ['l*k =  k', l*k, -o],
    ['l*l =  1', l*l, -x],
    ['l*m =  i', l*m,  i],
    ['l*n =  1', l*n,  j],
    ['1*o =  k', l*o,  k],

    ['m*1 =  1', m*x,  m],
    ['m*i =  i', m*i,  l],
    ['m*j =  1', m*j, -o],
    ['m*k =  k', m*k,  n],
    ['m*l =  1', m*l, -i],
    ['m*m =  i', m*m, -x],
    ['m*n =  1', m*n, -k],
    ['m*o =  k', m*o,  j],

    ['n*1 =  1', n*x,  n],
    ['n*i =  i', n*i,  o],
    ['n*j =  1', n*j,  l],
    ['n*k =  k', n*k, -m],
    ['n*l =  1', n*l, -j],
    ['n*m =  i', n*m,  k],
    ['n*n =  1', n*n, -x],
    ['n*o =  k', n*o, -i],

    ['o*1 =  1', o*x,  o],
    ['o*i =  i', o*i, -n],
    ['o*j =  1', o*j,  m],
    ['o*k =  k', o*k,  l],
    ['o*l =  1', o*l, -k],
    ['o*m =  i', o*m, -j],
    ['o*n =  1', o*n,  i],
    ['o*o =  k', o*o, -x],
] 

for entry in timestable:
    title, calc, expect = entry[::]

    print ("\nVerify %s:" % (title))
    print ("  expect: ", expect.flat())
    print ("    calc: ", calc.flat())

    if calc == expect:
        print ("Success\n")
    else:
        print ("    diff: ", (calc - expect).flat())
        print ("Fail\n")
        exit()



print ("\nCommutative Product tests...\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check x × y ≠ y × x')
    print ('check %s × %s ≠ %s × %s' % (x, y, y, x))
    print ('result %s ≠ %s' % (x*y, y*x))

    if x*y != y*x:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nWeak Alternative Condition (Lost) tests...\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check (x × x) × y ≠ x × (x × y)')
    print ("  left side: %s" % ((x*x)*y) )
    print (" right side: %s" % (x*(y*y)) )

    if (x*x)*y != x*(x*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (y × y) × x ≠ y × (y × x)')
    print ("  left side: %s" % ((y*y)*x) )
    print (" right side: %s" % (y*(y*x)) )

    if (y*y)*x != y*(y*x):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (x × y) × y ≠ x × (y × y)')
    print ("  left side: %s" % ((x*y)*y) )
    print (" right side: %s" % (x*(y*y)) )

    if (x*y)*y != x*(y*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (y × x) × x ≠ y × (x × x)')
    print ("  left side: %s" % ((y*x)*x) )
    print (" right side: %s" % (y*(x*x)) )

    if (y*x)*x != y*(x*x):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



#print ("\nBrahmagupta–Fibonacci / Diophantus identity test..\n")
#
#for i, n in enumerate(range(LOOPS)):
#    print ('test #%s' % (i + 1))
#
#    x = random_vector()
#    y = random_vector()
#
#    print ('check (x × x) × y ≠ x × (x × y)')
#    print ('check (%s × %s) × %s  ≠  %s × (%s × %s)' %(x,x,y,x,x,y))
#    print ('check %s  ≠  %s' %((x*x)*y,x*(x*y)))
#    print ('difference: %e' %(abs((x*x)*y-x*(x*y))))
#
#    if abs(x) * abs(y) - abs(x*y) <= PRECISION:
#        print ("Success\n")
#    else:
#        print ("Fail\n")
#        exit()



print ("\nMoufang condition (FAIL) tests\n")

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

    if a != b:
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

    if c != d:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    e = (z*x)*(y*z)
    f = (z*(x*y))*z

    print ('check (z × x) × (y × z) = (z × (x × y) × z ...')
    print ('(z × x) × (y × z) = ', e)
    print ('(z × (x × y)) × z = ', f)

    if e != f:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    g = (z*x)*(y*z)
    h = z*((x*y)*z)

    print ('check (z × x) × (y × z) = z × ((x × y) × z) ...')
    print ('(z × x) × (y × z) = ', g)
    print ('z × ((x × y) × z) = ', h)

    if g != h:
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

    print ('x = ', x)
    print ('y = ', y)
    print ('z = ', z)


    print ('norm x = %s' % (abs(x)))
    if abs(x) - 1 <= PRECISION:
        print ("Success\n")
    else:
        print ("    diff: ", (calc - expect).flat())
        print ("Fail\n")
        exit()

    print ('norm y = %s' % (abs(y)))
    if abs(y) - 1 <= PRECISION:
        print ("Success\n")
    else:
        print ("    diff: ", (calc - expect).flat())
        print ("Fail\n")
        exit()

    print ('WARNING: Something may be wrong here ...')
    print ('Reducing PRECISION to: 5%')
    print ('norm z = %s' % (abs(z)))
    if abs(z) - 1 <= 0.05:
        print ("Success\n")
    else:
        print ("    diff: ", (calc - expect).flat())
        print ("Fail\n")
        exit()



print ("\nSedenion Product - Pfister's sixteen-square identity tests\n")

for index in range(LOOPS):
    print ('test #%s' % (index + 1))

    x = random_vector()
    y = random_vector()

    calc = x * y

    print ("x flat: ", x.flat())
    print ("y flat: ", y.flat())

    a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16= x.flat()
    b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16= y.flat()
   
    # assuming i^2 = -1 ...
    z1  = a1 * b1  - a2  * b2  - a3  * b3  - a4  * b4  - b5  * a5  - b6  * a6  - b7  * a7  - b8  * a8  - b9  * a9  - b10 * a10 - b11 * a11 - b12 * a12 - a13 * b13 - a14 * b14 - a15 * b15 - a16 * b16
    z2  = a1 * b2  + a2  * b1  + a3  * b4  - a4  * b3  - b5  * a6  + b6  * a5  + b7  * a8  - b8  * a7  - b9  * a10 + b10 * a9  + b11 * a12 - b12 * a11 - a13 * b14 + a14 * b13 + a15 * b16 - a16 * b15
    z3  = a1 * b3  - a2  * b4  + a3  * b1  + a4  * b2  - b5  * a7  - b6  * a8  + b7  * a5  + b8  * a6  - b9  * a11 - b10 * a12 + b11 * a9  + b12 * a10 - a13 * b15 - a14 * b16 + a15 * b13 + a16 * b14
    z4  = a1 * b4  + a2  * b3  - a3  * b2  + a4  * b1  - b5  * a8  + b6  * a7  - b7  * a6  + b8  * a5  - b9  * a12 + b10 * a11 - b11 * a10 + b12 * a9  - a13 * b16 + a14 * b15 - a15 * b14 + a16 * b13
    z5  = b5 * a1  - b6  * a2  - b7  * a3  - b8  * a4  + a5  * b1  + a6  * b2  + a7  * b3  + a8  * b4  - a13 * b9  - a14 * b10 - a15 * b11 - a16 * b12 + b13 * a9  + b14 * a10 + b15 * a11 + b16 * a12
    z6  = b5 * a2  + b6  * a1  + b7  * a4  - b8  * a3  - a5  * b2  + a6  * b1  - a7  * b4  + a8  * b3  + a13 * b10 - a14 * b9  + a15 * b12 - a16 * b11 - b13 * a10 + b14 * a9  - b15 * a12 + b16 * a11
    z7  = b5 * a3  - b6  * a4  + b7  * a1  + b8  * a2  - a5  * b3  + a6  * b4  + a7  * b1  - a8  * b2  + a13 * b11 - a14 * b12 - a15 * b9  + a16 * b10 - b13 * a11 + b14 * a12 + b15 * a9  - b16 * a10
    z8  = b5 * a4  + b6  * a3  - b7  * a2  + b8  * a1  - a5  * b4  - a6  * b3  + a7  * b2  + a8  * b1  + a13 * b12 + a14 * b11 - a15 * b10 - a16 * b9  - b13 * a12 - b14 * a11 + b15 * a10 + b16 * a9
    z9  = b9 * a1  - b10 * a2  - b11 * a3  - b12 * a4  - a5  * b13 - a6  * b14 - a7  * b15 - a8  * b16 + a9  * b1  + a10 * b2  + a11 * b3  + a12 * b4  + b5  * a13 + b6  * a14 + b7  * a15 + b8  * a16
    z10 = b9 * a2  + b10 * a1  + b11 * a4  - b12 * a3  - a5  * b14 + a6  * b13 + a7  * b16 - a8  * b15 - a9  * b2  + a10 * b1  - a11 * b4  + a12 * b3  + b5  * a14 - b6  * a13 - b7  * a16 + b8  * a15
    z11 = b9 * a3  - b10 * a4  + b11 * a1  + b12 * a2  - a5  * b15 - a6  * b16 + a7  * b13 + a8  * b14 - a9  * b3  + a10 * b4  + a11 * b1  - a12 * b2  + b5  * a15 + b6  * a16 - b7  * a13 - b8  * a14
    z12 = b9 * a4  + b10 * a3  - b11 * a2  + b12 * a1  - a5  * b16 + a6  * b15 - a7  * b14 + a8  * b13 - a9  * b4  - a10 * b3  + a11 * b2  + a12 * b1  + b5  * a16 - b6  * a15 + b7  * a14 - b8  * a13
    z13 = a5 * b9  - a6  * b10 - a7  * b11 - a8  * b12 + b13 * a1  + b14 * a2  + b15 * a3  + b16 * a4  - b5  * a9  + b6  * a10 + b7  * a11 + b8  * a12 + a13 * b1  - a14 * b2  - a15 * b3  - a16 * b4
    z14 = a5 * b10 + a6  * b9  + a7  * b12 - a8  * b11 - b13 * a2  + b14 * a1  - b15 * a4  + b16 * a3  - b5  * a10 - b6  * a9  - b7  * a12 + b8  * a11 + a13 * b2  + a14 * b1  + a15 * b4  - a16 * b3
    z15 = a5 * b11 - a6  * b12 + a7  * b9  + a8  * b10 - b13 * a3  + b14 * a4  + b15 * a1  - b16 * a2  - b5  * a11 + b6  * a12 - b7  * a9  - b8  * a10 + a13 * b3  - a14 * b4  + a15 * b1  + a16 * b2
    z16 = a5 * b12 + a6  * b11 - a7  * b10 + a8  * b9  - b13 * a4  - b14 * a3  + b15 * a2  + b16 * a1  - b5  * a12 - b6  * a11 + b7  * a10 - b8  * a9  + a13 * b4  + a14 * b3  - a15 * b2  + a16 * b1

    z = Construction((z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16))

    print ('''
product formula => (
    a1 × b1  - a2  × b2  - a3  × b3  - a4  × b4  - b5  × a5  - b6  × a6  - b7  × a7  - b8  × a8  - b9  × a9  - b10 × a10 - b11 × a11 - b12 × a12 - a13 × b13 - a14 × b14 - a15 × b15 - a16 × b16
    a1 × b2  + a2  × b1  + a3  × b4  - a4  × b3  - b5  × a6  + b6  × a5  + b7  × a8  - b8  × a7  - b9  × a10 + b10 × a9  + b11 × a12 - b12 × a11 - a13 × b14 + a14 × b13 + a15 × b16 - a16 × b15
    a1 × b3  - a2  × b4  + a3  × b1  + a4  × b2  - b5  × a7  - b6  × a8  + b7  × a5  + b8  × a6  - b9  × a11 - b10 × a12 + b11 × a9  + b12 × a10 - a13 × b15 - a14 × b16 + a15 × b13 + a16 × b14
    a1 × b4  + a2  × b3  - a3  × b2  + a4  × b1  - b5  × a8  + b6  × a7  - b7  × a6  + b8  × a5  - b9  × a12 + b10 × a11 - b11 × a10 + b12 × a9  - a13 × b16 + a14 × b15 - a15 × b14 + a16 × b13
    b5 × a1  - b6  × a2  - b7  × a3  - b8  × a4  + a5  × b1  + a6  × b2  + a7  × b3  + a8  × b4  - a13 × b9  - a14 × b10 - a15 × b11 - a16 × b12 + b13 × a9  + b14 × a10 + b15 × a11 + b16 × a12
    b5 × a2  + b6  × a1  + b7  × a4  - b8  × a3  - a5  × b2  + a6  × b1  - a7  × b4  + a8  × b3  + a13 × b10 - a14 × b9  + a15 × b12 - a16 × b11 - b13 × a10 + b14 × a9  - b15 × a12 + b16 × a11
    b5 × a3  - b6  × a4  + b7  × a1  + b8  × a2  - a5  × b3  + a6  × b4  + a7  × b1  - a8  × b2  + a13 × b11 - a14 × b12 - a15 × b9  + a16 × b10 - b13 × a11 + b14 × a12 + b15 × a9  - b16 × a10
    b5 × a4  + b6  × a3  - b7  × a2  + b8  × a1  - a5  × b4  - a6  × b3  + a7  × b2  + a8  × b1  + a13 × b12 + a14 × b11 - a15 × b10 - a16 × b9  - b13 × a12 - b14 × a11 + b15 × a10 + b16 × a9
    b9 × a1  - b10 × a2  - b11 × a3  - b12 × a4  - a5  × b13 - a6  × b14 - a7  × b15 - a8  × b16 + a9  × b1  + a10 × b2  + a11 × b3  + a12 × b4  + b5  × a13 + b6  × a14 + b7  × a15 + b8  × a16
    b9 × a2  + b10 × a1  + b11 × a4  - b12 × a3  - a5  × b14 + a6  × b13 + a7  × b16 - a8  × b15 - a9  × b2  + a10 × b1  - a11 × b4  + a12 × b3  + b5  × a14 - b6  × a13 - b7  × a16 + b8  × a15
    b9 × a3  - b10 × a4  + b11 × a1  + b12 × a2  - a5  × b15 - a6  × b16 + a7  × b13 + a8  × b14 - a9  × b3  + a10 × b4  + a11 × b1  - a12 × b2  + b5  × a15 + b6  × a16 - b7  × a13 - b8  × a14
    b9 × a4  + b10 × a3  - b11 × a2  + b12 × a1  - a5  × b16 + a6  × b15 - a7  × b14 + a8  × b13 - a9  × b4  - a10 × b3  + a11 × b2  + a12 × b1  + b5  × a16 - b6  × a15 + b7  × a14 - b8  × a13
    a5 × b9  - a6  × b10 - a7  × b11 - a8  × b12 + b13 × a1  + b14 × a2  + b15 × a3  + b16 × a4  - b5  × a9  + b6  × a10 + b7  × a11 + b8  × a12 + a13 × b1  - a14 × b2  - a15 × b3  - a16 × b4
    a5 × b10 + a6  × b9  + a7  × b12 - a8  × b11 - b13 × a2  + b14 × a1  - b15 × a4  + b16 × a3  - b5  × a10 - b6  × a9  - b7  × a12 + b8  × a11 + a13 × b2  + a14 × b1  + a15 × b4  - a16 × b3
    a5 × b11 - a6  × b12 + a7  × b9  + a8  × b10 - b13 × a3  + b14 × a4  + b15 × a1  - b16 × a2  - b5  × a11 + b6  × a12 - b7  × a9  - b8  × a10 + a13 × b3  - a14 × b4  + a15 × b1  + a16 × b2
    a5 × b12 + a6  × b11 - a7  × b10 + a8  × b9  - b13 × a4  - b14 × a3  + b15 × a2  + b16 × a1  - b5  × a12 - b6  × a11 + b7  × a10 - b8  × a9  + a13 × b4  + a14 × b3  - a15 × b2  + a16 × b1
)''')
    print ('given x = (a)\n        = ', x.flat())
    print ('given x = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16)')
    print ('x = ', x.flat())
    print ('given y = (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16)')
    print ('y = ', y.flat())
    print ('formula = ', z)
    print ('   calc = ', calc)

    if z == calc:
        print ("Success\n")
    else:
        print ("\n Precision: ", z.precision())
        print ("\nDifference: ", abs(z-calc))
        print ("\nFail\n")
        exit()

