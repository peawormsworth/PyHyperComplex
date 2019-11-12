#!/usr/bin/python3
#
#  Test Complex, Quaternion, Octonion and Sedenion algebriac properties
#
#     file: t6_cayley_dickson.py
#   source: https://github.com/peawormsworth/PyHyperComplex
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     reference: https://en.wikipedia.org/wiki/Sedenion
#


import hypercomplex

from hypercomplex import Construction
from random       import random


LOOPS      = 10
PRECISION  = 10 ** -9
DIMENSIONS = [ 2, 4, 8, 16, 32, 64 ]


#
# generate a random complex number ...
#

def random_vector (dimension=2):
    return Construction([random() for _ in range(dimension)])


# 
# Cycle through tests, checking results appropriate for the current test dimension
#

for dimension in DIMENSIONS:

    print ("\n===\n===  DIMENSION: %s\n===" % (dimension))


    #
    # Multiplication Table tests
    #

    print ("\nMultiplication Table tests...\n")


    x = Construction((1,0) + (0,) * (dimension - 2 ))
    i = Construction((0,1) + (0,) * (dimension - 2 ))

    if dimension > 2:
        j = Construction((0,0,1,0) + (0,) * (dimension - 4))
        k = Construction((0,0,0,1) + (0,) * (dimension - 4))

    if dimension > 4:
        l = Construction((0,0,0,0,1,0,0,0) + (0,) * (dimension - 8))
        m = Construction((0,0,0,0,0,1,0,0) + (0,) * (dimension - 8))
        n = Construction((0,0,0,0,0,0,1,0) + (0,) * (dimension - 8))
        o = Construction((0,0,0,0,0,0,0,1) + (0,) * (dimension - 8))

    if dimension > 8:
        p = Construction((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0) + (0,) * (dimension - 16))
        q = Construction((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) + (0,) * (dimension - 16))
        r = Construction((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0) + (0,) * (dimension - 16))
        s = Construction((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0) + (0,) * (dimension - 16))
        t = Construction((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) + (0,) * (dimension - 16))
        u = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0) + (0,) * (dimension - 16))
        v = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0) + (0,) * (dimension - 16))
        w = Construction((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1) + (0,) * (dimension - 16))


    timestable = [

        ['1*1 =  1', x*x,  x],
        ['1*i =  i', x*i,  i],
        ['i*1 =  i', i*x,  i],
        ['i*i = -1', i*i, -x],
    ]

    if dimension > 2:
           
        timestable += [
            ['1*j =  1', x*j,  j],
            ['1*k =  k', x*k,  k],
            ['i*j =  k', i*j,  k],
            ['i*k = -j', i*k, -j],
            ['j*1 =  j', j*x,  j],
            ['j*i = -k', j*i, -k],
            ['j*j = -1', j*j, -x],
            ['j*k =  i', j*k,  i],
            ['k*1 =  k', k*x,  k],
            ['k*i =  j', k*i,  j],
            ['k*j = -i', k*j, -i],
            ['k*k = -1', k*k, -x],
        ]

    if dimension > 4:
        timestable += [
            ['1*l =  1', x*l,  l],
            ['1*m =  m', x*m,  m],
            ['1*n =  n', x*n,  n],
            ['1*o =  o', x*o,  o],
            ['i*l =  m', i*l,  m],
            ['i*m = -l', i*m, -l],
            ['i*n = -o', i*n, -o],
            ['i*o =  n', i*o,  n],
            ['j*l =  n', j*l,  n],
            ['j*m =  o', j*m,  o],
            ['j*n = -l', j*n, -l],
            ['j*o = -m', j*o, -m],
            ['k*l =  o', k*l,  o],
            ['k*m = -n', k*m, -n],
            ['k*n =  m', k*n,  m],
            ['k*o = -l', k*o, -l],
            ['l*1 =  1', l*x,  l],
            ['l*i = -m', l*i, -m],
            ['l*j = -n', l*j, -n],
            ['l*k = -o', l*k, -o],
            ['l*l = -1', l*l, -x],
            ['l*m =  i', l*m,  i],
            ['l*n =  j', l*n,  j],
            ['1*o =  k', l*o,  k],
            ['m*1 =  m', m*x,  m],
            ['m*i =  l', m*i,  l],
            ['m*j = -o', m*j, -o],
            ['m*k =  n', m*k,  n],
            ['m*l = -i', m*l, -i],
            ['m*m = -1', m*m, -x],
            ['m*n = -k', m*n, -k],
            ['m*o =  j', m*o,  j],
            ['n*1 =  n', n*x,  n],
            ['n*i =  o', n*i,  o],
            ['n*j =  l', n*j,  l],
            ['n*k = -m', n*k, -m],
            ['n*l = -j', n*l, -j],
            ['n*m =  k', n*m,  k],
            ['n*n = -1', n*n, -x],
            ['n*o = -i', n*o, -i],
            ['o*1 =  o', o*x,  o],
            ['o*i = -n', o*i, -n],
            ['o*j =  m', o*j,  m],
            ['o*k =  l', o*k,  l],
            ['o*l = -k', o*l, -k],
            ['o*m = -j', o*m, -j],
            ['o*n =  i', o*n,  i],
            ['o*o = -1', o*o, -x],
        ]

    if dimension > 8:
        timestable += [
            ['1*p =  p', x*p,  p],
            ['1*q =  q', x*q,  q],
            ['1*r =  r', x*r,  r],
            ['1*s =  s', x*s,  s],
            ['1*t =  t', x*t,  t],
            ['1*u =  u', x*u,  u],
            ['1*v =  v', x*v,  v],
            ['1*w =  w', x*w,  w],
            ['i*p =  i', i*p,  q],
            ['i*q = -x', i*q, -p],
            ['i*r =  k', i*r, -s],
            ['i*s = -j', i*s,  r],
            ['i*t =  m', i*t, -u],
            ['i*u = -l', i*u,  t],
            ['i*v = -o', i*v,  w],
            ['i*w =  n', i*w, -v],
            ['j*p =  1', j*p,  r],
            ['j*q =  i', j*q,  s],
            ['j*r =  1', j*r, -p],
            ['j*s =  k', j*s, -q],
            ['j*t =  1', j*t, -v],
            ['j*u =  i', j*u, -w],
            ['j*v =  1', j*v,  t],
            ['j*w =  k', j*w,  u],
            ['k*p =  1', k*p,  s],
            ['k*q =  i', k*q, -r],
            ['k*r =  1', k*r,  q],
            ['k*s =  k', k*s, -p],
            ['k*t =  1', k*t, -w],
            ['k*u =  i', k*u,  v],
            ['k*v =  1', k*v, -u],
            ['k*w =  k', k*w,  t],
            ['l*p =  1', l*p,  t],
            ['l*q =  i', l*q,  u],
            ['l*r =  1', l*r,  v],
            ['l*s =  k', l*s,  w],
            ['l*t =  1', l*t, -p],
            ['l*u =  i', l*u, -q],
            ['l*v =  1', l*v, -r],
            ['1*w =  k', l*w, -s],
            ['m*p =  1', m*p,  u],
            ['m*q =  i', m*q, -t],
            ['m*r =  1', m*r,  w],
            ['m*s =  k', m*s, -v],
            ['m*t =  1', m*t,  q],
            ['m*u =  i', m*u, -p],
            ['m*v =  1', m*v,  s],
            ['m*w =  k', m*w, -r],
            ['n*p =  1', n*p,  v],
            ['n*q =  i', n*q, -w],
            ['n*r =  1', n*r, -t],
            ['n*s =  k', n*s,  u],
            ['n*t =  1', n*t,  r],
            ['n*u =  i', n*u, -s],
            ['n*v =  1', n*v, -p],
            ['n*w =  k', n*w,  q],
            ['o*p =  1', o*p,  w],
            ['o*q =  i', o*q,  v],
            ['o*r =  1', o*r, -u],
            ['o*s =  k', o*s, -t],
            ['o*t =  1', o*t,  s],
            ['o*u =  i', o*u,  r],
            ['o*v =  1', o*v, -q],
            ['o*w =  k', o*w, -p],
            ['p*1 =  p', p*x,  p],
            ['p*i = -q', p*i, -q],
            ['p*j = -r', p*j, -r],
            ['p*k = -s', p*k, -s],
            ['p*l = -t', p*l, -t],
            ['p*m = -u', p*m, -u],
            ['p*n = -v', p*n, -v],
            ['p*o = -w', p*o, -w],
            ['p*p = -1', p*p, -x],
            ['p*q =  i', p*q,  i],
            ['p*r =  j', p*r,  j],
            ['p*s =  k', p*s,  k],
            ['p*t =  l', p*t,  l],
            ['p*u =  m', p*u,  m],
            ['p*v =  n', p*v,  n],
            ['p*w =  o', p*w,  o],
            ['q*1 =  q', q*x,  q],
            ['q*i =  p', q*i,  p],
            ['q*j = -s', q*j, -s],
            ['q*k =  r', q*k,  r],
            ['q*l = -u', q*l, -u],
            ['q*m =  t', q*m,  t],
            ['q*n =  w', q*n,  w],
            ['q*o = -v', q*o, -v],
            ['q*p = -i', q*p, -i],
            ['q*q = -1', q*q, -x],
            ['q*r = -k', q*r, -k],
            ['q*s =  j', q*s,  j],
            ['q*t = -m', q*t, -m],
            ['q*u =  l', q*u,  l],
            ['q*v =  o', q*v,  o],
            ['q*w = -n', q*w, -n],
            ['r*1 =  r', r*x,  r],
            ['r*i =  s', r*i,  s],
            ['r*j =  p', r*j,  p],
            ['r*k = -q', r*k, -q],
            ['r*l = -v', r*l, -v],
            ['r*m = -w', r*m, -w],
            ['r*n =  t', r*n,  t],
            ['r*o =  u', r*o,  u],
            ['r*p = -j', r*p, -j],
            ['r*q =  k', r*q,  k],
            ['r*r = -1', r*r, -x],
            ['r*s = -i', r*s, -i],
            ['r*t = -n', r*t, -n],
            ['r*u = -o', r*u, -o],
            ['r*v =  l', r*v,  l],
            ['r*w =  m', r*w,  m],
            ['s*1 =  s', s*x,  s],
            ['s*i = -r', s*i, -r],
            ['s*j =  q', s*j,  q],
            ['s*k =  p', s*k,  p],
            ['s*l = -w', s*l, -w],
            ['s*m =  v', s*m,  v],
            ['s*n = -u', s*n, -u],
            ['s*o =  t', s*o,  t],
            ['s*p = -k', s*p, -k],
            ['s*q = -j', s*q, -j],
            ['s*r =  i', s*r,  i],
            ['s*s = -1', s*s, -x],
            ['s*t = -o', s*t, -o],
            ['s*u =  n', s*u,  n],
            ['s*v = -m', s*v, -m],
            ['s*w =  l', s*w,  l],
            ['t*1 =  t', t*x,  t],
            ['t*i =  u', t*i,  u],
            ['t*j =  v', t*j,  v],
            ['t*k =  w', t*k,  w],
            ['t*l =  p', t*l,  p],
            ['t*m = -q', t*m, -q],
            ['t*n = -r', t*n, -r],
            ['t*o = -s', t*o, -s],
            ['t*p = -l', t*p, -l],
            ['t*q =  m', t*q,  m],
            ['t*r =  n', t*r,  n],
            ['t*s =  o', t*s,  o],
            ['t*t = -1', t*t, -x],
            ['t*u = -i', t*u, -i],
            ['t*v = -j', t*v, -j],
            ['t*w = -k', t*w, -k],
            ['u*1 =  u', u*x,  u],
            ['u*i = -t', u*i, -t],
            ['u*j =  w', u*j,  w],
            ['u*k = -v', u*k, -v],
            ['u*l =  q', u*l,  q],
            ['u*m =  p', u*m,  p],
            ['u*n =  s', u*n,  s],
            ['u*o = -r', u*o, -r],
            ['u*p = -m', u*p, -m],
            ['u*q = -l', u*q, -l],
            ['u*r =  o', u*r,  o],
            ['u*s = -n', u*s, -n],
            ['u*t =  i', u*t,  i],
            ['u*u = -1', u*u, -x],
            ['u*v =  k', u*v,  k],
            ['u*w = -j', u*w, -j],
            ['v*1 =  v', v*x,  v],
            ['v*i = -w', v*i, -w],
            ['v*j = -t', v*j, -t],
            ['v*k =  u', v*k,  u],
            ['v*l =  r', v*l,  r],
            ['v*m = -s', v*m, -s],
            ['v*n =  p', v*n,  p],
            ['v*o =  q', v*o,  q],
            ['v*p = -n', v*p, -n],
            ['v*q = -o', v*q, -o],
            ['v*r = -l', v*r, -l],
            ['v*s =  m', v*s,  m],
            ['v*t =  j', v*t,  j],
            ['v*u = -k', v*u, -k],
            ['v*v = -1', v*v, -x],
            ['v*w =  i', v*w,  i],
            ['w*1 =  w', w*x,  w],
            ['w*i =  v', w*i,  v],
            ['w*j = -u', w*j, -u],
            ['w*k = -t', w*k, -t],
            ['w*l =  s', w*l,  s],
            ['w*m =  r', w*m,  r],
            ['w*n = -q', w*n, -q],
            ['w*o =  p', w*o,  p],
            ['w*p = -o', w*p, -o],
            ['w*q =  n', w*q,  n],
            ['w*r = -m', w*r, -m],
            ['w*s = -l', w*s, -l],
            ['w*t =  k', w*t,  k],
            ['w*u =  j', w*u,  j],
            ['w*v = -i', w*v, -i],
            ['w*w = -1', w*w, -x],
        ] 

    for entry in timestable:
        title, calc, expect = entry[::]

        #print ("Verify: %s" % (title))
        #print ("  expect: ", expect.flat())
        #print ("    calc: ", calc.flat())
        #print ("      expect: ", expect)
        #print ("        calc: ", calc)

        if calc == expect:
            print ("Verify %s: Success" %(title))
        else:
            print ("%s: Fail" %(title))
            print ("    diff: ", (calc - expect).flat())
            exit()


    #
    # Commutative Product tests
    #

    print ("\nCommutative Product tests...\n")

    for i, n in enumerate(range(LOOPS)):
        print ('test #%s' % (i + 1))

        x = random_vector(dimension)
        y = random_vector(dimension)

        if dimension > 2:
            print ('check x × y ≠ y × x')
            print ('check %s × %s ≠ %s × %s' % (x.flat(), y.flat(), y.flat(), x.flat()))
            print ('result %s ≠ %s' % ((x*y).flat(), (y*x).flat()))

            if x*y != y*x:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

        else:
            print ('check x × y = y × x')
            print ('check %s × %s = %s × %s' % (x.flat(), y.flat(), y.flat(), x.flat()))
            print ('result %s = %s' % ((x*y).flat(), (y*x).flat()))

            if x*y == y*x:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()



    #
    # Weak Alternative Condition tests
    #

    print ("\nWeak Alternative Condition (Lost) tests...\n")

    for i, n in enumerate(range(LOOPS)):
        print ('test #%s' % (i + 1))

        x = random_vector(dimension)
        y = random_vector(dimension)

        if dimension > 8:
            print ('check (x × x) × y ≠ x × (x × y)')
            print ("  left side:", ((x*x)*y).flat() )
            print (" right side:", (x*(y*y)).flat() )

            if (x*x)*y != x*(x*y):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (y × y) × x ≠ y × (y × x)')
            print ("  left side:", ((y*y)*x).flat() )
            print (" right side:", (y*(y*x)).flat() )

            if (y*y)*x != y*(y*x):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (x × y) × y ≠ x × (y × y)')
            print ("  left side:", ((x*y)*y).flat() )
            print (" right side:", (x*(y*y)).flat() )

            if (x*y)*y != x*(y*y):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (y × x) × x ≠ y × (x × x)')
            print ("  left side:", ((y*x)*x).flat() )
            print (" right side:", (y*(x*x)).flat() )

            if (y*x)*x != y*(x*x):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()


        else:
            print ('check (x × x) × y = x × (x × y)')
            print ("  left side:", ((x*x)*y).flat() )
            print (" right side:", (x*(y*y)).flat() )

            if (x*x)*y == x*(x*y):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (y × y) × x = y × (y × x)')
            print ("  left side:", ((y*y)*x).flat() )
            print (" right side:", (y*(y*x)).flat() )

            if (y*y)*x == y*(y*x):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (x × y) × y = x × (y × y)')
            print ("  left side:", ((x*y)*y).flat() )
            print (" right side:", (x*(y*y)).flat() )

            if (x*y)*y == x*(y*y):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            print ('check (y × x) × x = y × (x × x)')
            print ("  left side:", ((y*x)*x).flat() )
            print (" right side:", (y*(x*x)).flat() )

            if (y*x)*x == y*(x*x):
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()



    #
    # Diophantus identity test
    #

    print ("\nBrahmagupta–Fibonacci / Diophantus identity test..\n")

    for i, n in enumerate(range(LOOPS)):
        print ('test #%s' % (i + 1))

        x = random_vector(dimension)
        y = random_vector(dimension)

        if dimension > 8:
            print ('check |x| × |y| ≠ |x × y|')
            print ("\n Precision: ", PRECISION)
            print ('difference: %e' %(abs(x) * abs(y) - abs(x*y)))

            if (abs(abs(x) * abs(y) - abs(x*y))) <= PRECISION:
                print ("Success\n")
                print ("Failure was expected, so: Fail\n")
                exit()
            else:
                print ("Fail")
                print ("Failure was expected, so: Success\n")


        else:
            print ('check |x| × |y| ≠ |= × y|')
            print ("\n Precision: ", PRECISION)
            print ('difference: %e' %(abs(x) * abs(y) - abs(x*y)))

            if (abs(abs(x) * abs(y) - abs(x*y))) <= PRECISION:
                print ("Success\n")
            else:
                print ("Fail")
                exit()



    #
    # Moufang condition tests
    #

    print ("\nMoufang condition (FAIL) tests\n")

    for i, n in enumerate(range(LOOPS)):
        print ('test #%s' % (i + 1))

        x = random_vector(dimension)
        y = random_vector(dimension)
        z = random_vector(dimension)

        print ('x = %s\ny = %s\nz = %s' % (x.flat(),y.flat(),z.flat()))

        a = z*(x*(z*y))
        b = ((z*x)*z)*y

        if dimension > 8:

            print ('z × (x × (z × y)) = ((z × x) × z) × y ...')
            print ('z × (x × (z × y)) =', a.flat() )
            print ('((z × x) × z) × y =', b.flat() )

            if a != b:
                print ("Success\n")
            else:
                print ("    diff: ", abs(a - b))
                print ("Fail\n")
                exit()

            c = x*(z*(y*z))
            d = ((x*z)*y)*z

            print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
            print ('x × (z × (y × z)) = ', c.flat() )
            print ('((x × z) × y) × z = ', d.flat() )

            if c != d:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            e = (z*x)*(y*z)
            f = (z*(x*y))*z

            print ('check (z × x) × (y × z) = (z × (x × y) × z ...')
            print ('(z × x) × (y × z) = ', e.flat() )
            print ('(z × (x × y)) × z = ', f.flat() )

            if e != f:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            g = (z*x)*(y*z)
            h = z*((x*y)*z)

            print ('check (z × x) × (y × z) = z × ((x × y) × z) ...')
            print ('(z × x) × (y × z) = ', g.flat() )
            print ('z × ((x × y) × z) = ', h.flat() )

            if g != h:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()


        else:

            print ('z × (x × (z × y)) = ((z × x) × z) × y ...')
            print ('z × (x × (z × y)) =', a.flat() )
            print ('((z × x) × z) × y =', b.flat() )

            if a == b:
                print ("Success\n")
            else:
                print ("    diff: ", abs(a - b))
                print ("Fail\n")
                exit()

            c = x*(z*(y*z))
            d = ((x*z)*y)*z

            print ('check x × (z × (y × z)) = ((x × z) × y) × z ...')
            print ('x × (z × (y × z)) = ',  c.flat() )
            print ('((x × z) × y) × z = ',  d.flat() )

            if c == d:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            e = (z*x)*(y*z)
            f = (z*(x*y))*z

            print ('check (z × x) × (y × z) = (z × (x × y) × z ...')
            print ('(z × x) × (y × z) = ',  e.flat() )
            print ('(z × (x × y)) × z = ',  f.flat() )

            if e == f:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

            g = (z*x)*(y*z)
            h = z*((x*y)*z)

            print ('check (z × x) × (y × z) = z × ((x × y) × z) ...')
            print ('(z × x) × (y × z) = ',  g.flat() )
            print ('z × ((x × y) × z) = ',  h.flat() )

            if g == h:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()



    #
    # Power Associative tests
    #

    print ("\nPower Associative tests\n")

    for i, n in enumerate(range(LOOPS)):
        print ('test #%s' % (i + 1))

        x = random_vector(dimension).normalize()
        y = random_vector(dimension).normalize()
        z = x * y

        print ('x = ', x.flat())
        print ('y = ', y.flat())
        print ('z = ', z.flat())


        print ('norm x = %s' % (abs(x)))
        if abs(abs(x) - 1) <= PRECISION:
            print ("Success\n")
        else:
            print ("    diff: ", abs(calc - expect))
            print ("Fail\n")
            exit()

        print ('norm y = %s' % (abs(y)))
        if (abs(y) - 1) <= PRECISION:
            print ("Success\n")
        else:
            print ("    diff: ", abs(calc - expect))
            print ("Fail\n")
            exit()

        print ('norm z = %s' % (abs(z)))
        if (abs(z) - 1) <= PRECISION:
            print ("Success\n")
        else:
            print ('Reducing PRECISION to: 5%')
            if (abs(z) - 1) <= 0.05:
                print ('WARNING: Low precision. Something may be wrong here. ...')
                print ("Success\n")
            else:
                print ("    diff: ", abs(calc - expect))
                print ("Fail\n")
                exit()



    #
    # Square identity tests
    #

    print ("\nHyper Complex Product - member of square identity tests\n")

    for index in range(LOOPS):
        print ('test #%s' % (index + 1))

        x = random_vector(dimension)
        y = random_vector(dimension)

        calc = x * y

        print ("x flat: ", x.flat())
        print ("y flat: ", y.flat())

        if dimension == 2:

            #
            # Two square identity
            #

            print ("\nComplex Product - Two square identity\n")

            a = x.a
            b = x.b
            c = y.a
            d = y.b

            z = x * y
            m = Construction((a*c - d*b, d*a + b*c))

            print ('x × y = (a,b) × (c,d) = (ac-db,da+bc)')
            print ('a = %s\nb = %s\nc = %s\nd = %s' % (a, b, c, d))
            print ('(ac-db,da+bc) = %s' % (m))
            print ('        x × y = %s' % (z))

            if z == m:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()

        elif dimension == 4:

            #
            #
            #

            a,b,c,d = x.flat()
            e,f,g,h = y.flat()
           
            # assuming i^2 = -1 ...
            r = a*e-b*f-c*g-d*h
            s = a*f+b*e+c*h-d*g
            t = a*g-b*h+c*e+d*f
            u = a*h+b*g-c*f+d*e

            z = x *y
            m = Construction((r,s,t,u))

            print ('product formula => (a,b,c,d) × (c,d,e,f) = (ae-bf-cg-dh, af+be+ch-dg, ag-bh+ce+df, ah+bg-cf+de)')
            print ('given x = (a,b,c,d) = ', x.flat())
            print ('given y = (e,f,g,h) = ', y.flat())
            print ('so m = (ae-bf-cg-dh,\n        af+be+ch-dg,\n        ag-bh+ce+df,\n        ah+bg-cf+de) = %s' % (m))
            print ('           z = x × y = %s' % (z))

            if z == m:
                print ("Success\n")
            else:
                print ("Fail\n")
                exit()



        elif dimension == 8:

            #
            # Octonion Product - Eight Square Identity test
            #

            print ("\nOctonion Product - Eight Square Identity test\n")

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



        elif dimension == 16:

            #
            #
            #

            print ("\nSedenion Product - Pfister's sixteen-square identity\n")

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


        else:
            print ("\nwarning: * no product formula available at these dimensions *\n")
           


