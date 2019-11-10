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
    return Construction((random(), random(), random(), random(), random(), random(), random(), random()))


print ("\nMultiplication Table tests...\n")

x = Construction((1,0,0,0,0,0,0,0))
i = Construction((0,1,0,0,0,0,0,0))
j = Construction((0,0,1,0,0,0,0,0))
k = Construction((0,0,0,1,0,0,0,0))
l = Construction((0,0,0,0,1,0,0,0))
m = Construction((0,0,0,0,0,1,0,0))
n = Construction((0,0,0,0,0,0,1,0))
o = Construction((0,0,0,0,0,0,0,1))

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
    print ("    diff: ", (calc - expect).flat())

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



print ("\nOctonion Product - Eight Square Identity tests\n")

for index in range(LOOPS):
    print ('test #%s' % (index + 1))

    x = random_vector()
    y = random_vector()

    calc = x * y

    print ("x flat: ", x.flat())
    print ("y flat: ", y.flat())

    a,b,c,d,e,f,g,h = x.flat()
    i,j,k,l,m,n,o,p = y.flat()
   
    # assuming i^2 = -1 ...
    z1 = a*i - b*j - c*k - d*l - m*e - n*f - o*g - p*h
    z2 = a*j + b*i + c*l - d*k - m*f + n*e + o*h - p*g
    z3 = a*k - b*l + c*i + d*j - m*g - n*h + o*e + p*f
    z4 = a*l + b*k - c*j + d*i - m*h + n*g - o*f + p*e
    z5 = m*a - n*b - o*c - p*d + e*i + f*j + g*k + h*l
    z6 = m*b + n*a + o*d - p*c - e*j + f*i - g*l + h*k
    z7 = m*c - n*d + o*a + p*b - e*k + f*l + g*i - h*j
    z8 = m*d + n*c - o*b + p*a - e*l - f*k + g*j + h*i

    z = Construction((z1,z2,z3,z4,z5,z6,z7,z8))

    print ('''product formula => (
    ai - bj - ck - dl - me - nf - og - ph,
    aj + bi + cl - dk - mf + ne + oh - pg,
    ak - bl + ci + dj - mg - nh + oe + pf,
    al + bk - cj + di - mh + ng - of + pe,
    ma - nb - oc - pd + ei + fj + gk + hl,
    mb + na + od - pc - ej + fi - gl + hk,
    mc - nd + oa + pb - ek + fl + gi - hj,
    md + nc - ob + pa - el - fk + gj + hi,
)''')
    print ('given x = (a,b,c,d,e,f,g,h)\n        = ', x.flat())
    print ('given y = (i,j,k,l,m,n,o,p) = ', y.flat())
    print ('formula = ', z)
    print ('   calc = ', calc)

    if z == calc:
        print ("Success\n")
    else:
        print ("\n Precision: ", z.precision())
        print ("\nDifference: ", abs(z-calc))
        print ("\nFail\n")
        exit()

