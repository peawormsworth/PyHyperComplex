#!/usr/bin/python3
#
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     reference: https://en.wikipedia.org/wiki/Quaternion
#

import hypercomplex

from hypercomplex import Construction
from random       import random


LOOPS = 20
PRECISION = 10 ** -9


# generate a random complex number ...
#
def random_vector ():
    return Construction((random(), random(), random(), random()))


print ("\nMultiplication Table tests...\n")

x = Construction((1,0,0,0))
i = Construction((0,1,0,0))
j = Construction((0,0,1,0))
k = Construction((0,0,0,1))

timestable = [
    ['1*1 =  1', x*x,  x],
    ['1*i =  i', x*i,  i],
    ['1*j =  1', x*j,  j],
    ['1*k =  k', x*k,  k],
    ['i*1 =  i', i*x,  i],
    ['i*i = -1', i*i, -x],
    ['i*j =  k', i*j,  k],
    ['i*k = -j', i*k, -j],
    ['j*1 =  j', j*x,  j],
    ['j*i = -k', j*i, -k],
    ['j*j = -x', j*j, -x],
    ['j*k =  i', j*k,  i],
    ['k*1 =  k', k*x,  k],
    ['k*i =  j', k*i,  j],
    ['k*j = -i', k*j, -i],
    ['k*k = -x', k*k, -x]
]

for entry in timestable:
    title, calc, expect = entry[::]

    print ("\nVerify %s:" % (title))
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

    print ('check x × y ≠ y × x')
    print ('check %s × %s ≠ %s × %s' % (x, y, y, x))
    print ('result %s ≠ %s' % (x*y, y*x))

    if x*y != y*x:
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
    print ("  left side: %s" % ((x*x)*y) )
    print (" right side: %s" % (x*(y*y)) )

    if (x*x)*y == x*(x*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (y × y) × x = y × (y × x)')
    print ("  left side: %s" % ((y*y)*x) )
    print (" right side: %s" % (y*(y*x)) )

    if (y*y)*x == y*(y*x):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (x × y) × y = x × (y × y)')
    print ("  left side: %s" % ((x*y)*y) )
    print (" right side: %s" % (x*(y*y)) )

    if (x*y)*y == x*(y*y):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

    print ('check (y × x) × x = y × (x × x)')
    print ("  left side: %s" % ((y*x)*x) )
    print (" right side: %s" % (y*(x*x)) )

    if (y*x)*x == y*(x*x):
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()



print ("\nBrahmagupta–Fibonacci / Diophantus identity test..\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    print ('check (x × x) × y ≠ x × (x × y)')
    print ('check (%s × %s) × %s  ≠  %s × (%s × %s)' %(x,x,y,x,x,y))
    print ('check %s  ≠  %s' %((x*x)*y,x*(x*y)))
    print ('difference: %e' %(abs((x*x)*y-x*(x*y))))

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

    print ('x = ', x)
    print ('y = ', y)
    print ('z = ', z)

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



print ("\nQuaternion Product - Euler's Four Square Identity tests\n")

for i, n in enumerate(range(LOOPS)):
    print ('test #%s' % (i + 1))

    x = random_vector()
    y = random_vector()

    z = x * y

    (a,b,c,d) = x.flat()
    (e,f,g,h) = y.flat()
   
    # assuming i^2 = -1 ...
    r = a*e-b*f-c*g-d*h
    s = a*f+b*e+c*h-d*g
    t = a*g-b*h+c*e+d*f
    u = a*h+b*g-c*f+d*e
    m = Construction((r,s,t,u))

    print ('product formula => (a,b,c,d) × (c,d,e,f) = (ae-bf-cg-dh, af+be+ch-dg, ag-bh+ce+df, ah+bg-cf+de)')
    print ('given x = (a,b,c,d) = ', x)
    print ('given y = (e,f,g,h) = ', y)
    print ('so m = (ae-bf-cg-dh,\n        af+be+ch-dg,\n        ag-bh+ce+df,\n        ah+bg-cf+de) = %s' % (m))
    print ('           z = x × y = %s' % (z))

    if z == m:
        print ("Success\n")
    else:
        print ("Fail\n")
        exit()

