#!/usr/bin/python3
#
#  Hypercomplex - Unit Tests
#
#    general class wide, product table, algebraic, identity and quantum emulation tests
#
#     file: test_hypercomplex.py
#   source: https://github.com/peawormsworth/PyHyperComplex
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#

import unittest

from hypercomplex import Construction as Construct
from hypercomplex import RootFraction
from random       import random
from math         import pi as π
from math         import sqrt


def random_vector ():
    return Construct((random(), random()))


#
# Attributes test
#
class TestAttributes(unittest.TestCase):
    ATTRIBUTES = [
        '__add__',     '__radd__',    '__rsub__',    '__sub__',       '__rmul__',    '__rtruediv__',
        '__truediv__', '__mul__',     '__abs__',     '__invert__',    '__pow__',     '__neg__',
        '__pos__',     '__iadd__',    '__isub__',    '__imul__',      '__idiv__',    '__eq__', 
        '__getitem__', '__getitem__', '__repr__',    '__str__',       '__init__',    '__ne__',
        '__complex__', 'log',         'conj',        'norm',          'normalize',   'geodesic_norm',
        'tensor',      'is_real',     'is_complex',  'is_quaternion', 'is_octonion', 'is_sedenion',
        'flat',        'a',           'b',           're',            'im'
    ]
    def test_attribute (self):
        z = random_vector()
        for attribute in self.ATTRIBUTES:
            self.assertTrue(attribute in dir(z))


#
# Right/Left order operator tests
#
class TestRightLeftOperators(unittest.TestCase):
    loops = 1

    def test_left_right_multiplication (self, loops=loops):
        for n in range(loops):
            z1 = random_vector()
            z2 = random_vector()
            self.assertEqual(z1*z2, z2*z1, "%s != %s" % (z1*z2, z2*z1))

    def test_right_left_addition (self, loops = loops):
        for n in range(loops):
            z1 = random_vector()
            z2 = random_vector()
            self.assertEqual(z1+z2, z2+z1, "%s != %s" % (z1+z2, z2+z1))

    def test_right_left_subtraction (self, loops=loops):
        for n in range(loops):
            z1 = random_vector()
            z2 = random_vector()
            self.assertEqual(z1-z2, -(z2-z1), "%s != %s" % (z1-z2, -(z2-z1)))


#
# Dimension type matching 
#
class TestDimensions(unittest.TestCase):
    LOOPS = 1

    def test_complex_dimensions (self):
        for n in range(self.LOOPS):

            z = Construct([random() for _ in range(2)])
            self.assertTrue(z.is_complex())
            self.assertFalse(z.is_quaternion())
            self.assertFalse(z.is_octonion())
            self.assertFalse(z.is_sedenion())
            self.assertNotEqual(z.dimension(), 32)

    def test_quaternion_dimensions (self):
        for n in range(self.LOOPS):

            z = Construct([random() for _ in range(4)])
            self.assertFalse(z.is_complex())
            self.assertTrue(z.is_quaternion())
            self.assertFalse(z.is_octonion())
            self.assertFalse(z.is_sedenion())
            self.assertNotEqual(z.dimension(), 32)

    def test_octonion_dimensions (self):
        for n in range(self.LOOPS):

            z = Construct([random() for _ in range(8)])
            self.assertFalse(z.is_complex())
            self.assertFalse(z.is_quaternion())
            self.assertTrue(z.is_octonion())
            self.assertFalse(z.is_sedenion())
            self.assertNotEqual(z.dimension(), 32)

    def test_sedenion_dimensions (self):
        for n in range(self.LOOPS):

            z = Construct([random() for _ in range(16)])
            self.assertFalse(z.is_complex())
            self.assertFalse(z.is_quaternion())
            self.assertFalse(z.is_octonion())
            self.assertTrue(z.is_sedenion())
            self.assertNotEqual(z.dimension(), 32)

    def test_32ion (self):
        for n in range(self.LOOPS):

            z = Construct([random() for _ in range(32)])
            self.assertFalse(z.is_complex())
            self.assertFalse(z.is_quaternion())
            self.assertFalse(z.is_octonion())
            self.assertFalse(z.is_sedenion())
            self.assertEqual(z.dimension(), 32)


#
# Multiplication Table tests
#
class TestMultiplicationTable (unittest.TestCase):

    def test_complex_unit_table (self):
        x = Construct((1,0))
        i = Construct((0,1))
        timestable = [
            ['1*1 =  1', x*x,  x],
            ['1*i =  i', x*i,  i],
            ['i*1 =  i', i*x,  i],
            ['i*i = -1', i*i, -x],
        ]
        for entry in timestable:
            title, calc, expect = entry[::]
            self.assertEqual(calc, expect)

    def test_quaternion_unit_table (self):
        x = Construct((1,0,0,0))
        i = Construct((0,1,0,0))
        j = Construct((0,0,1,0))
        k = Construct((0,0,0,1))
        timestable = [
            ['1*1 =  1', x*x,  x],
            ['1*i =  i', x*i,  i],
            ['i*1 =  i', i*x,  i],
            ['i*i = -1', i*i, -x],
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
        for entry in timestable:
            title, calc, expect = entry[::]
            self.assertEqual(calc, expect)
 

    def test_octonion_unit_table (self):
        x = Construct((1,0,0,0,0,0,0,0))
        i = Construct((0,1,0,0,0,0,0,0))
        j = Construct((0,0,1,0,0,0,0,0))
        k = Construct((0,0,0,1,0,0,0,0))
        l = Construct((0,0,0,0,1,0,0,0))
        m = Construct((0,0,0,0,0,1,0,0))
        n = Construct((0,0,0,0,0,0,1,0))
        o = Construct((0,0,0,0,0,0,0,1))
        timestable = [
            ['1*1 =  1', x*x,  x],
            ['1*i =  i', x*i,  i],
            ['i*1 =  i', i*x,  i],
            ['i*i = -1', i*i, -x],
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
        for entry in timestable:
            title, calc, expect = entry[::]
            self.assertEqual(calc, expect)

    def test_sedenion_unit_table (self):
        x = Construct((1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        i = Construct((0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        j = Construct((0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0))
        k = Construct((0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0))
        l = Construct((0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0))
        m = Construct((0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0))
        n = Construct((0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0))
        o = Construct((0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0))
        p = Construct((0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0))
        q = Construct((0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0))
        r = Construct((0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0))
        s = Construct((0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0))
        t = Construct((0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0))
        u = Construct((0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0))
        v = Construct((0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0))
        w = Construct((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1))
        timestable = [
            ['1*1 =  1', x*x,  x],
            ['1*i =  i', x*i,  i],
            ['i*1 =  i', i*x,  i],
            ['i*i = -1', i*i, -x],
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
            self.assertEqual(calc, expect)

 
#
# Commutative Product tests
#
class TestCommutative (unittest.TestCase):
    LOOPS = 10
    def _is_commutative (self, dimensions=0):
        for n in range(self.LOOPS):
            x = random_vector(dimensions)
            y = random_vector(dimensions)
            if dimensions > 2:
                self.assertNotEqual(x*y,y*x)
            else:
                self.assertEqual(x*y,y*x)
        
    def test_complex (self):
        self._is_commutative(dimensions=2)

    def test_quaternion (self):
        self._is_commutative(dimensions=4)

    def test_octonion (self):
        self._is_commutative(dimensions=8)

    def test_sedenion (self):
        self._is_commutative(dimensions=16)

    def test_32ion (self):
        self._is_commutative(dimensions=32)

    def test_64ion (self):
        self._is_commutative(dimensions=64)


#
# Weak Alternative Condition tests
#
class TestWeakAlternativeCondition (unittest.TestCase):
    LOOPS = 1
    def _is_weak_alternative(self, dimensions=0):
        for n in range(self.LOOPS):
            x = random_vector(dimensions)
            y = random_vector(dimensions)
            if dimensions < 16:
                self.assertEqual((y*x)*x, y*(x*x))
                self.assertEqual((x*y)*x, x*(y*x))
                self.assertEqual((x*x)*y, x*(x*y))
                self.assertEqual((x*y)*y, x*(y*y))
                self.assertEqual((y*x)*y, y*(x*y))
                self.assertEqual((y*y)*x, y*(y*x))
            else:
                self.assertEqual((x*y)*x, x*(y*x))
                self.assertEqual((y*x)*y, y*(x*y))
                self.assertNotEqual((y*x)*x, y*(x*x))
                self.assertNotEqual((x*x)*y, x*(x*y))
                self.assertNotEqual((x*y)*y, x*(y*y))
                self.assertNotEqual((y*y)*x, y*(y*x))

    def test_complex (self):
        self._is_weak_alternative(dimensions=2)

    def test_quaternion (self):
        self._is_weak_alternative(dimensions=4)

    def test_octonion (self):
        self._is_weak_alternative(dimensions=8)

    def test_sedenion (self):
        self._is_weak_alternative(dimensions=16)

    def test_32ion (self):
        self._is_weak_alternative(dimensions=32)

    def test_64ion (self):
        self._is_weak_alternative(dimensions=64)


#
# Diophantus identity test
#  Brahmagupta–Fibonacci / Diophantus identity
#
class TestDiophantusIdentity (unittest.TestCase):
    PRECISION = 10**-9
    LOOPS = 1
    def _is_diophantus_identity(self, dimensions=0):
        for n in range(self.LOOPS):
            x = random_vector(dimensions)
            y = random_vector(dimensions)
            if dimensions > 8:
                self.assertNotAlmostEqual(abs(x) * abs(y), abs(x*y), delta=self.PRECISION)
            else:
                self.assertAlmostEqual(abs(x) * abs(y), abs(x*y), delta=self.PRECISION)

    def test_complex (self):
        self._is_diophantus_identity(dimensions=2)

    def test_quaternion (self):
        self._is_diophantus_identity(dimensions=4)

    def test_octonion (self):
        self._is_diophantus_identity(dimensions=8)

    def test_sedenion (self):
        self._is_diophantus_identity(dimensions=16)

    def test_32ion (self):
        self._is_diophantus_identity(dimensions=32)

    def test_64ion (self):
        self._is_diophantus_identity(dimensions=64)


#
# Moufang condition tests
#
class TestMoufangCondition (unittest.TestCase):
    LOOPS = 1
    def _is_moufang_condition(self, dimensions=0):
        for n in range(self.LOOPS):
            x = random_vector(dimensions)
            y = random_vector(dimensions)
            z = random_vector(dimensions)
            a = z*(x*(z*y))
            b = ((z*x)*z)*y
            c = x*(z*(y*z))
            d = ((x*z)*y)*z
            e = (z*x)*(y*z)
            f = (z*(x*y))*z
            g = (z*x)*(y*z)
            h = z*((x*y)*z)
            if dimensions > 8:
                self.assertNotEqual(a,b)
                self.assertNotEqual(c,d)
                self.assertNotEqual(e,f)
                self.assertNotEqual(g,h)
            else:
                self.assertEqual(a,b)
                self.assertEqual(c,d)
                self.assertEqual(e,f)
                self.assertEqual(g,h)

    def test_complex (self):
        self._is_moufang_condition(dimensions=2)

    def test_quaternion (self):
        self._is_moufang_condition(dimensions=4)

    def test_octonion (self):
        self._is_moufang_condition(dimensions=8)

    def test_sedenion (self):
        self._is_moufang_condition(dimensions=16)

    def test_32ion (self):
        self._is_moufang_condition(dimensions=32)

    def test_64ion (self):
        self._is_moufang_condition(dimensions=64)


#
# Power Associative tests
#
class TestPowerAssociative (unittest.TestCase):
    PRECISION = 10**-9
    LOOPS = 1
    def _is_power_associative(self, dimensions=0):
        for n in range(self.LOOPS):
            x = random_vector(dimensions).normalize()
            y = random_vector(dimensions).normalize()
            z = x * y
            self.assertAlmostEqual(abs(x),1,delta=self.PRECISION)
            self.assertAlmostEqual(abs(y),1,delta=self.PRECISION)
            if dimensions > 8:
                self.assertAlmostEqual(abs(z),1,delta=10**-1)
            else:
                self.assertAlmostEqual(abs(z),1,delta=self.PRECISION)

    def test_complex (self):
        self._is_power_associative(dimensions=2)

    def test_quaternion (self):
        self._is_power_associative(dimensions=4)

    def test_octonion (self):
        self._is_power_associative(dimensions=8)

    def test_sedenion (self):
        self._is_power_associative(dimensions=16)

    def test_32ion (self):
        self._is_power_associative(dimensions=32)

    def test_64ion (self):
        self._is_power_associative(dimensions=64)


#
# Two square identity
#
class TestTwoSquareIdentity (unittest.TestCase):

    def test_two_square_identity (self):
        x = random_vector(2)
        y = random_vector(2)
        a, b = x
        c, d = y
        form = Construct((a*c - d*b, d*a + b*c))
        self.assertEqual(form, x*y)


#
# Four square identity
#
class TestFourSquareIdentity (unittest.TestCase):
    def test_four_square_identity (self):
        x = random_vector(4)
        y = random_vector(4)
        a,b,c,d = x
        e,f,g,h = y
        r = a*e - b*f - c*g - d*h
        s = a*f + b*e + c*h - d*g
        t = a*g - b*h + c*e + d*f
        u = a*h + b*g - c*f + d*e
        form = Construct((r,s,t,u))
        self.assertEqual(form, x*y)


#
# Eight square identity
#
class TestEightSquareIdentity (unittest.TestCase):
    def test_eight_square_identity (self):
        x = random_vector(8)
        y = random_vector(8)
        a,b,c,d,e,f,g,h = x
        i,j,k,l,m,n,o,p = y
        # assuming i^2 = -1 ...
        z1 = a*i - b*j - c*k - d*l - m*e - n*f - o*g - p*h
        z2 = a*j + b*i + c*l - d*k - m*f + n*e + o*h - p*g
        z3 = a*k - b*l + c*i + d*j - m*g - n*h + o*e + p*f
        z4 = a*l + b*k - c*j + d*i - m*h + n*g - o*f + p*e
        z5 = m*a - n*b - o*c - p*d + e*i + f*j + g*k + h*l
        z6 = m*b + n*a + o*d - p*c - e*j + f*i - g*l + h*k
        z7 = m*c - n*d + o*a + p*b - e*k + f*l + g*i - h*j
        z8 = m*d + n*c - o*b + p*a - e*l - f*k + g*j + h*i
        form = Construct((z1,z2,z3,z4,z5,z6,z7,z8))
        self.assertEqual(form, x*y)


#
# Sixteen square identity
#
class TestSixteenSquareIdentity (unittest.TestCase):
    def test_sixteen_square_identity (self):
        x = random_vector(16)
        y = random_vector(16)
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16 = x
        b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16 = y
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
        form = Construct((z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16))
        self.assertEqual(form, x*y)


#
# Quatum Tests
#
class TestQuantumEmulator (unittest.TestCase):
    gate_cnot     = Construct((sqrt(1/2), sqrt(1/2),0,0))
    gate_x        = Construct((0, 1))
    gate_hadamard = Construct((sqrt(1/2), sqrt(1/2)))

    def cnot(self, z1,z2):
        c = z1.tensor(z2)
        return self.gate_cnot * c * ~ self.gate_cnot

    def xgate(self, z):
        return self.gate_x / z

    def hadamard(self, z):
        return self.gate_hadamard / z


    def test_instantiate (self):
        for t in [(1,2),(3,4),(-1,2)]:
            self.assertEqual(RootFraction(t).flat(), t)

    def test_tensor (self):
        z1 = Construct((1,2))
        z2 = Construct((3,4))
        z  = Construct((1,0))
        o  = Construct((0,1))
        brakets = [
            [ z1.tensor(z2), (3,4,6,8) ],
            [ o.tensor(z.tensor(z)), (0,0,0,0,1,0,0,0) ],
            [ o.tensor(z.tensor(o)), (0,0,0,0,0,1,0,0) ],
            [ o.tensor(o.tensor(z)), (0,0,0,0,0,0,1,0) ],
            [ o.tensor(o.tensor(o)), (0,0,0,0,0,0,0,1) ],
            [ o.tensor(z.tensor(z.tensor(z))), (0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(z.tensor(o))), (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(z))), (0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(z))), (0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0) ],
            [ o.tensor(o.tensor(o.tensor(z))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0) ],
            [ o.tensor(o.tensor(o.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1) ],
            [ o.tensor(z.tensor(z.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(z.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(z.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(z.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0) ],
            [ o.tensor(z.tensor(o.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0) ],
            [ o.tensor(o.tensor(z.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0) ],
            [ o.tensor(o.tensor(o.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) ],
            [ o.tensor(o.tensor(o.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0) ],
            [ o.tensor(o.tensor(o.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0) ],
            [ o.tensor(o.tensor(o.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1) ],
        ]
        for item in brakets:
            calc, expected = item
            expect = Construct(expected)
            self.assertEqual(calc, expect)

    #
    # XGATE: Flip along √i axis. 1 => 0, 0 => 1
    #
    def test_xgate (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        zz = z.tensor(z)
        zo = z.tensor(o)
        oz = o.tensor(z)
        oo = o.tensor(o)
        rz = self.hadamard(z)
        ro = self.hadamard(o)
        cnot_tests = [
            [ 'Verify XGATE +|0>| = +|1>', self.xgate( z),  o ],
            [ 'Verify XGATE +|1>| = +|0>', self.xgate( o),  z ],
            [ 'Verify XGATE -|0>| = -|1>', self.xgate(-z), -o ],
            [ 'Verify XGATE -|1>| = -|0>', self.xgate(-o), -z ],
            [ 'Verify XGATE |00>| = |10>', self.xgate(zz), oz ],
            [ 'Verify XGATE |01>| =-|11>', self.xgate(zo),-oo ],
            [ 'Verify XGATE |10>| = |10>', self.xgate(oz), zz ],
            [ 'Verify XGATE |11>| = |01>', self.xgate(oo), zo ],
        ]
        for test in cnot_tests:
            title, calc, expect = test
            self.assertEqual(calc, expect)

    #
    # CNOT: second bit flip controlled by the first
    #
    def test_cnot (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        cnot_tests = [
            [ 'Verify CNOT |00>| =  |00>', self.cnot(z,z), (1, 0, 0, 0) ],
            [ 'Verify CNOT |01>| =  |01>', self.cnot(z,o), (0, 1, 0, 0) ],
            [ 'Verify CNOT |10>| =  |11>', self.cnot(o,z), (0, 0, 0, 1) ],
            [ 'Verify CNOT |11>| = -|10>', self.cnot(o,o), (0, 0,-1, 0) ]
        ]
        for test in cnot_tests:
            title, calc, expected = test
            expect = Construct(expected)
            self.assertEqual(calc, expect)

    #
    # Hadamard gate test
    #
    def test_hadamard (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        zz = z.tensor(z)
        zo = z.tensor(o)
        oz = o.tensor(z)
        oo = o.tensor(o)
        rz = self.hadamard(z)
        ro = self.hadamard(o)
        hadamard_tests = [
            [ 'Verify HADAMARD +| 0>| = + | +>', self.hadamard( z), rz ],
            [ 'Verify HADAMARD +| 1>| = + | ->', self.hadamard( o), ro ],
            [ 'Verify HADAMARD -| 0>| = - | +>', self.hadamard(-z),-rz ],
            [ 'Verify HADAMARD -| 1>| = - | ->', self.hadamard(-o),-ro ],
            [ 'Verify HADAMARD +|00>| = + |1+>', self.hadamard(zz), rz.tensor(z) ],
            [ 'Verify HADAMARD +|01>| = - |11>', self.hadamard(zo), -rz.tensor(o) ],
            [ 'Verify HADAMARD +|10>| = + |00>', self.hadamard(oz), ro.tensor(z) ],
            [ 'Verify HADAMARD +|11>| = + |01>', self.hadamard(oo), ro.tensor(o) ],
        ]
        for test in hadamard_tests:
            title, calc, expected = test
            #expect = Construct(expected)
            self.assertEqual(calc, expected)

    #
    # 16 Step Circle Walk test
    #
    def test_16_steps (self):
        z = Construct((1,0))
        steps = [
            (0,1),
            (sqrt(1/2),-sqrt(1/2)),
            (-sqrt(1/2),sqrt(1/2)),
            (0,-1),
            (-1,0),
            (-sqrt(1/2),-sqrt(1/2)),
            (-sqrt(1/2),-sqrt(1/2)),
            (-1,0),
            (0,-1),
            (-sqrt(1/2),sqrt(1/2)),
            (sqrt(1/2),-sqrt(1/2)),
            (0,1),
            (1,0),
            (sqrt(1/2),sqrt(1/2)),
            (sqrt(1/2),sqrt(1/2)),
            (1,0),
        ]
        starting = Construct((z.flat()))
        for i in range(16):
            if i % 2:
                gate = 'Hadamard'
                z2 = self.hadamard(z)
            else:
                gate = '   XGate'
                z2 = self.xgate(z)

            z = z2
            self.assertEqual(z, Construct(steps[i]))
        self.assertEqual(z, starting)


#
# Black box: constant 0, constant 1, identity and negate
#
class TestBlackBox (unittest.TestCase):
    gate_cnot     = Construct((sqrt(1/2), sqrt(1/2),0,0))
    gate_x        = Construct((0, 1))
    gate_hadamard = Construct((sqrt(1/2), sqrt(1/2)))

    def cnot(self, z1,z2):
        c = z1.tensor(z2)
        return self.gate_cnot * c * ~ self.gate_cnot

    def xgate(self, z):
        return self.gate_x / z

    def hadamard(self, z):
        return self.gate_hadamard / z

    def test_constant_0 (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        control = Construct(z.flat())
        target  = Construct(z.flat())
        self.assertEqual(control, z)
        self.assertEqual(target,  z)
        control = Construct(o.flat())
        target  = Construct(z.flat())
        self.assertEqual(control, o)
        self.assertEqual(target,  z)

    def test_constant_1 (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        control = z.copy()
        target  = z.copy()
        target  = self.xgate(target)
        self.assertEqual(control, z)
        self.assertEqual(target,  o)
        control = o.copy()
        target  = z.copy()
        target  = self.xgate(target)
        self.assertEqual(control, o)
        self.assertEqual(target,  o)

    def test_identity (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        control = z.copy()
        target  = z.copy()
        self.cnot(control, target)
        self.assertEqual(control, z)
        self.assertEqual(target,  z)
        control = o.copy()
        target  = z.copy()
        self.cnot(control, target)
        self.assertEqual(control, o)
        self.assertEqual(target,  z)


    def test_negate (self):
        z  = Construct((1,0))
        o  = Construct((0,1))
        control = z.copy()
        target  = z.copy()
        self.cnot(control, target)
        target  = self.xgate(target)
        self.assertEqual(control, z)
        self.assertEqual(target,  o)
        control = o.copy()
        target  = z.copy()
        self.cnot(control, target)
        target  = self.xgate(target)
        self.assertEqual(control, o)
        self.assertEqual(target,  o)


#
# generate a random complex number ...
#
def random_vector (dimension=2):
    return Construct([random() for _ in range(dimension)])


if __name__ == '__main__':

    unittest.main()
