#
#   hypercomplex.Construction
#
#     python class for Cayley Dickson number construction and operation
#
#     source: https://github.com/peawormsworth/PyCayleyDickson
#     author: Jeffrey B Anderson - truejeffanderson at gmail.com
#

import math

class Construction(object):
    isquare = -1
    precision = 10 ** -9

    #
    #  Addition: z1+z2 = (a,b)+(c,d) = (a+c,b+d)
    #
    def __add__ (self, z):
        try:
            a, b = self.a + z.a, self.b + z.b
        except:
            a, b = self.a + z, self.b
        return self.__class__((a, b))

    #
    # reverse Addition
    #
    def __radd__ (self, z):
        return self + z

    #
    # referse Subtract
    #
    def __rsub__ (self, z):
        return -self + z

    #
    # Subtraction: (a,b)-(c,d) = (a-c,b-d)
    #
    def __sub__ (self, z):
        return self + -z

    #
    # Reverse Multiplication
    #
    def __rmul__ (self, z):
        return self * z

    #
    # Reverse Division
    #
    def __rtruediv__ (self, z):
        return ~self * z

    #
    # Division: z1/z2 = (a,b) × (c,d)⁻¹ = (a,b) × inverse(c,d)
    #
    def __truediv__ (self, z):
        if isinstance(z, Construction):
            return  ~z * self
        else:
            return 1/z * self

    #
    # Multiplication: (a,b)×(c,d) = (a×c - d*×b, d×a + b×c*) 
    #   where x* = conjugate(x) or x if x is a number
    #
    def __mul__ (self, z):
        a  = self.a
        b  = self.b
        try:
            c = z.a
        except:
            c = z
        try:
            d = z.b
        except:
            d = 0
        try:
            ac = a.conj()
        except:
            ac = a
        try:
            bc = b.conj()
        except:
            bc = b
        try:
            cc = c.conj()
        except:
            cc = c
        try:
            dc = d.conj()
        except:
            dc = d
        return self.__class__(self.doubling_product(a,b,c,d,ac,bc,cc,dc))

    #
    # Doubling Product: multiplication rules for (a,b)×(c,d)
    #   given the values a,b,c,d,a★,b★,c★,d★
    #  where z★ = conjugate of z
    #
    def doubling_product (self,a,b,c,d,ac,bc,cc,dc):
        return (a*c + self.isquare * dc*b, d*a + b*cc)

    #
    # Absolute Value = Norm: √(norm(a)²+norm(b)²)
    #
    def __abs__ (self):
        return math.sqrt(abs(self.a) ** 2 + abs(self.b) ** 2)

    #
    # Invert: z⁻¹
    #
    def __invert__ (self):
        return self.conj()  / abs(self) ** 2

    #
    # Power: z^x
    #
    def __pow__ (self, power):
        return abs(self) ** power * (math.cos(power * abs(self.im())) + self.im().normalize() * math.sin(power * abs(self.im())))

    #
    # Negate: -z = -1 × z
    #
    def __neg__ (self):
        return -1 * self

    #
    # Positive: +z = z
    #
    def __pos__ (self):
        return self

    #
    # Replace: the existing coefficients with those of the given one
    #
    def replace (self, z):
        self.a(z.a)
        self.b(z.b)
        return self

    #
    # Addition with assignment: z += x
    #
    def __iadd__ (self, z):
        return self.replace(self.__add__(z))

    #
    # Subtraction with assignment: z -= x
    #
    def __isub__ (self, z):
        return self.replace(self.__sub__(z))

    #
    # Multiplication with assignment: z *= x
    #
    def __imul__ (self, z):
        return self.replace(self.__mul__(z))

    #
    # Division with assignment: z /= x
    #
    def __idiv__ (self, z):
        return self.replace(self.__div__(z))

    #
    # Power with assignment: z **= x
    #
    def __ipow__ (self, z):
        return self.replace(self.__pow__(z))

    #
    # Equality condition: true if z = x
    #
    def __eq__ (self, z):
        #return (self - z).norm() <= self.precision
        return abs(self - z) <= self.precision

    #
    # Inequality: true is z ≠ x
    #
    def __ne__ (self, z):
        return not self == z

    #
    #  automatically generate a Complex object using the weight of a and b 
    #    as the real and imaginary components
    #
    def __complex__ (self):
       return complex( float(abs(self.a)), float(abs(self.b)) )

    #
    #  the power to which e mush be raised to obtain this number
    #  if this number is z, then log(z) returns the x, so that e^x = z
    #  Log: log(z) = x, so that e^x = z
    #
    def log (self):
        return math.log(abs(self.im())) + self.im().normalize() * math.acos(self.re() / abs(self))

    # 
    #  Conjugate: z* = (a,b)* = (a*,-b)
    #
    def conj (self):
        try:
            ac = self.a.conj()
        except:
            ac = self.a
        return self.__class__((ac, -self.b))

    #
    # Norm: √(norm(a)²+norm(b)²) and norm(number) = number
    #
    def norm (self):
        return abs(self)

    #
    # Normalize: z/|z| = zn, where norm of zn = 1
    #
    def normalize (self):
        return self / abs(self)

    #
    # Geodesic Norm: gn(z,x) = |ln(z⁻¹x)|
    # ref: https://en.wikipedia.org/wiki/Quaternion#Geodesic_norm
    #
    def geodesic_norm (self, z):
        return abs(log(~self * z))

    #
    # Tensor: $a->tensor($b) = A ⊗ B = (a,b) ⊗ (c,d) = (ac,ad,bc,bd)
    #
    def tensor (self, z):
        try:
            return self.__class__((self.a.tensor(z), self.b.tensor(z)))
        except:
            return self.__class__((z * self.a,  z * self.b))

    #
    # return dimension count for this number
    #
    def dimension(self):
        return len(self.flat())

    #
    # return the Cayley Dickson level for this number
    # where level = log2(dim)
    #   level 0 = 1d
    #   level 1 = 2d
    #   level 2 = 4d
    #   level 3 = 8d
    #   level 4 = 16d
    #    ...etc...
    #
    def level (self):
        return math.log(self.dimension()) / math.log(2)

    #
    # confirm the imaginary portions of the number are zero
    #
    def is_real (self):
        return not self.im

    #
    # confirm this number is a 2d Complex number
    #
    def is_complex (self):
        return self.level() == 1

    #
    # confirm this number is a 4d Quaternion number
    #
    def is_quaternion  (self):
        return self.level() == 2

    #
    # confirm this number is a 8d Octonion number
    #
    def is_octonion (self):
        return self.level() == 3

    #
    # confirm this number is a 16d Sedenion number
    #
    def is_sedenion (self):
        return self.level() == 4

    #
    # initialize a new object request
    #   expects a 2^n element tuple parameter
    #
    def __init__ (self, list):
        h = len(list) // 2
        if h > 1:
            self.a(self.__class__((list[:h])))
            self.b(self.__class__((list[h:])))
        elif h < 1:
            self.a(list[0])
            self.b(0)
        else:
            self.a(list[0])
            self.b(list[1])

    #
    # a: left half of number
    #
    def a (self, a=None):
        if a is not None:
            self.a = a
        return self.a

    #
    # b: right half of number
    #
    def b (self, b=None):
        if b is not None:
            self.b = b
        return self.b

    #
    # Real part of number
    #
    def re (self):
        return self[0]

    #
    # Imaginary part of number
    #
    def im (self):
        return self.__class__(((0,) + self[1:]))

    #
    # return the coefficient of the basis for the provided index
    #
    def __getitem__ (self, index):
        return self.flat()[index]

    #
    # return an ordered list of the coefficients
    #
    def flat (self):
        try:
           return self.a.flat() + self.b.flat()
        except:
           return (self.a, self.b)

    #
    # copy this object state to a new one...
    #
    def copy (self):
        return self.__class__(self.flat())

    #
    # String format:
    #   ordered imaginary units: i, j, k, etc.
    #   no basis is shown for real units
    #   no leading positive symbol
    #
    def __str__ (self):
        string = ''
        if abs(self):
            for index, coefficient in enumerate(self.flat()):
                if coefficient != 0: 
                    sign = ''
                    if coefficient < 0: 
                        sign = '-' 
                    elif len(string):
                        sign = '+'
                    value = abs(coefficient)
                    if index:
                        unit = chr(ord('i') + index - 1)
                    else:
                        unit = ''
                    string = string + sign + str(value) + unit
        if string is None:
            string = '0'
        return string

    #
    # replicate: output this number as a string suitable for evaluation
    #
    def __repr__ (self):
        return "%r(%r)" % ( str(self.__class__.__name__), self[::] )

#
# RootFraction is a Construction with a different default string output.
#  the format is a root fraction, rather then a float or decimal.
#
#  sample class output: t5_quantum.py
#

from fractions import Fraction
from decimal   import Decimal

class RootFraction(Construction):

    def __str__ (self):
        string = ''
        if abs(self):
            for index, coefficient in enumerate(self.flat()):
                if coefficient != 0: 
                    sign = ''
                    if coefficient < 0: 
                        sign = '-'
                    #elif len(string):
                    else:
                        sign = '+'
                    if string != '':
                        sign = ' ' + sign + ' '
                    symbols = '₀₁₂₃₄₅₆₇₈₉'
                    #if index:
                    if 1:
                        unit = '·e'
                        #unit = 'e'
                        n = Decimal(index)
                        if n == 0:
                            unit = '·e₀'
                        digits = 0
                        while n >= 1:
                            digits += 1
                            n = n / 10
                        #while n > 0:
                        for _ in range(digits):
                            n *= 10
                            unit += symbols[math.floor(n)]
                            n -= math.floor(n)
                    else:
                        unit = 'e₀'
                    fraction = Fraction.from_float(float(abs(coefficient) ** 2)).limit_denominator(1000000)
                    value = '√%s/%s' %  (fraction.numerator, fraction.denominator)
                    if value == '√1/1':
                        #if unit == '':
                        if 1:
                            value = '1'
                        else:
                            value = ''
                    #string = string + sign + '·'.join([value, unit])
                    string = string + sign + value + unit
        if string is None:
            string = '0'
        string = '(' + string + ')'
        return string

