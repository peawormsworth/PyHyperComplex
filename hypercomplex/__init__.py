# $Id: hypercomplex.py $
# Author: Jeff Anderson <truejeffanderson@gmail.com>
# Copyright: AGPL
"""

hypercomplex.Construction

python class for Cayley Dickson number construction and operation

source: https://github.com/peawormsworth/PyCayleyDickson
author: Jeffrey B Anderson - truejeffanderson at gmail.com
"""

import math

class Construction(object):
    """
    A Cayley-Dickson construction class to create and manipulate extra 
    dimensional numbers. More information on these constructions here:

    see: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction

    Each object contains two numbers or two similar objects.

    An object with two numbers represents a complex number with 2 dimensions.
    An object containing two objects each having two numbers or a total of
    four numbers is a quaternion.

    'a', the left side of the objects content, contains the lower half of the
    dimensions of the number. The other half 'b' contains the values of the
    upper half of the dimensions.

    Math operations are overloaded making common manipulations simple.
    """

    isquare = -1
    precision = 10 ** -9

    def __add__ (self, z):
        """Addition: z1+z2 = (a,b)+(c,d) = (a+c,b+d) is called automatically when coding a+b"""
        try:
            a, b = self.a + z.a, self.b + z.b
        except:
            a, b = self.a + z, self.b
        return self.__class__((a, b))

    def __radd__ (self, z):
        """Called automatically when coding a+b, where a is a number and b is of this class"""
        return self + z

    def __rsub__ (self, z):
        """Called automatically when coding a-b, where a is a number and b is of this class"""
        return -self + z

    def __sub__ (self, z):
        """Subtraction: z1-z2 = (a,b)-(c,d) = (a-c,b-d) is called automatically when coding a-b"""
        return self + -z

    def __rmul__ (self, z):
        """Called automatically when coding a*b, where a is a number and b is of this class"""
        return self * z

    def __rtruediv__ (self, z):
        """Called automatically when coding a/b, where a is a number and b is of this class"""
        return ~self * z

    def __truediv__ (self, z):
        """Division: z1/z2 = (a,b) × (c,d)⁻¹ = (a,b) × inverse(c,d)"""
        if isinstance(z, Construction):
            return  ~z * self
        else:
            return 1/z * self

    def __mul__ (self, z):
        """
        Multiplication: (a,b)×(c,d) = (a×c - d*×b, d×a + b×c*)
        where x* = conjugate(x)
        """
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

    def doubling_product (self,a,b,c,d,ac,bc,cc,dc):
        """
        Doubling Product: multiplication rules for (a,b)×(c,d)
        given the values a,b,c,d,a★,b★,c★,d★
        where z★ = conjugate of z
        """
        return (a*c + self.isquare * dc*b, d*a + b*cc)

    def __abs__ (self):
        """Absolute Value = Norm: √(norm(a)²+norm(b)²). called with abs(obj)"""
        return math.sqrt(abs(self.a) ** 2 + abs(self.b) ** 2)

    def __invert__ (self):
        """Invert: z⁻¹. called with ~ object"""
        return self.conj()  / abs(self) ** 2

    def __pow__ (self, power):
        """Power: z^x. called automatically with obj**x"""
        abs_im  = abs(self.im())
        norm_im = self.im().normalize()
        return abs(self) ** power * (
            math.cos(power * abs_im) + norm_im * math.sin(power * abs_im)
        )

    def __neg__ (self):
        """Negate: -z = -1 × z. called automatically with -obj"""
        return -1 * self

    def __pos__ (self):
        """Positive: +z = z"""
        # CONSIDER: Should we return self or a copy of self?
        return self

    def replace (self, z):
        """Replace: the existing coefficients with those of the given one"""
        self.a(z.a)
        self.b(z.b)
        return self

    def __iadd__ (self, z):
        """Addition with assignment: z += x"""
        return self.replace(self.__add__(z))

    def __isub__ (self, z):
        """Subtraction with assignment: z -= x"""
        return self.replace(self.__sub__(z))

    def __imul__ (self, z):
        """Multiplication with assignment: z *= x"""
        return self.replace(self.__mul__(z))

    def __idiv__ (self, z):
        """Division with assignment: z /= x"""
        return self.replace(self.__div__(z))

    def __ipow__ (self, z):
        """Power with assignment: z **= x"""
        return self.replace(self.__pow__(z))

    def __eq__ (self, z):
        """Equality condition: true if z = x"""
        return abs(self - z) <= self.precision

    def __ne__ (self, z):
        """Inequality: true is z ≠ x"""
        return not self == z

    def __complex__ (self):
        """
        automatically generate a Complex object using the weight of a and b 
        as the real and imaginary components
        """
        return complex( float(abs(self.a)), float(abs(self.b)) ) 

    def log (self):
        """
        the power to which e mush be raised to obtain this number
        if this number is z, then log(z) returns the x, so that e^x = z
        Log: log(z) = x, so that e^x = z
        """
        im_norm = self.im().normalize()
        abs_im  = abs(self.im())
        return math.log(abs_im) + im_norm * math.acos(self.re() / abs(self))

    def conj (self):
        """
        Conjugate: z* = (a,b)* = (a*,-b)
        It is the negation of imaginary values
        x*=x when x is a real number
        """
        try:
            ac = self.a.conj()
        except:
            ac = self.a
        return self.__class__((ac, -self.b))

    def norm (self):
        """Norm: √(norm(a)²+norm(b)²) and norm(number) = number"""
        return abs(self)

    def normalize (self):
        """Normalize: z/|z| = zn, where norm of zn = 1"""
        return self / abs(self)

    def geodesic_norm (self, z):
       """
       Geodesic Norm: gn(z,x) = |ln(z⁻¹x)|
       ref: https://en.wikipedia.org/wiki/Quaternion#Geodesic_norm
       """
       return abs(log(~self * z))

    def tensor (self, z):
        """Tensor: $a->tensor($b) = A ⊗ B = (a,b) ⊗ (c,d) = (ac,ad,bc,bd)"""
        try:
            return self.__class__((self.a.tensor(z), self.b.tensor(z)))
        except:
            return self.__class__((z * self.a,  z * self.b))

    def dimension(self):
        """dimension count for this number"""
        return len(self.flat())

    def level (self):
        """
        return the Cayley Dickson level for this number
        where level = log2(dim)
        level 0 = 1d
        level 1 = 2d
        level 2 = 4d
        level 3 = 8d
        level 4 = 16d
        ...etc...
        """
        return math.log(self.dimension()) / math.log(2)

    def is_real (self):
        """confirm the imaginary portions of the number are zero"""
        return not self.im

    def is_complex (self):
        """confirm this number is a 2d Complex number"""
        return self.level() == 1

    def is_quaternion  (self):
        """confirm this number is a 4d Quaternion number"""
        return self.level() == 2

    def is_octonion (self):
        """confirm this number is a 8d Octonion number"""
        return self.level() == 3

    def is_sedenion (self):
        """confirm this number is a 16d Sedenion number"""
        return self.level() == 4

    def __init__ (self, list):
        """
        initialize a new object request
        expects a 2^n element tuple parameter
        """
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

    def a (self, a=None):
        """a: left half of number"""
        if a is not None:
            self.a = a
        return self.a

    def b (self, b=None):
        """b: right half of number"""
        if b is not None:
            self.b = b
        return self.b

    def re (self):
        """Real part of number"""
        return self[0]

    def im (self):
        """Imaginary part of number"""
        return self.__class__(((0,) + self[1:]))

    def __getitem__ (self, index):
        """the coefficient of the basis for the provided index"""
        return self.flat()[index]

    def flat (self):
        """return an ordered list of the coefficients"""
        try:
           return self.a.flat() + self.b.flat()
        except:
           return (self.a, self.b)

    def copy (self):
        """copy this object state to a new one..."""
        return self.__class__(self.flat())

    def __str__ (self):
        """
        String format:
        ordered imaginary units: i, j, k, etc.
        no basis is shown for real units
        no leading positive symbol
        """
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

    def __repr__ (self):
        """replicate: output this number as a string suitable for evaluation"""
        return "%r(%r)" % ( str(self.__class__.__name__), self[::] )

from fractions import Fraction
from decimal   import Decimal

class RootFraction(Construction):
    """
    RootFraction is a Construction with a different default string output.
    the format is a root fraction, rather then a float or decimal.
    """
    def __str__ (self):
        """
        string output coefficients returned as integer root fractions
        and numerically index basis units called 'e'
        """
        string = ''
        if abs(self):
            for index, coefficient in enumerate(self.flat()):
                if coefficient != 0: 
                    sign = ''
                    if coefficient < 0: 
                        sign = '-'
                    else:
                        sign = '+'
                    if string != '':
                        sign = ' ' + sign + ' '
                    symbols = '₀₁₂₃₄₅₆₇₈₉'
                    unit = '·e'
                    n = Decimal(index)
                    if n == 0:
                        unit = '·e₀'
                    digits = 0
                    while n >= 1:
                        digits += 1
                        n = n / 10
                    for _ in range(digits):
                        n *= 10
                        unit += symbols[math.floor(n)]
                        n -= math.floor(n)
                    else:
                        unit = 'e₀'
                    fraction = Fraction \
                        .from_float(float(abs(coefficient) ** 2)) \
                        .limit_denominator(1000000)
                    value = '√%s/%s' %  (fraction.numerator, fraction.denominator)
                    if value == '√1/1':
                        value = '1'
                    string = string + sign + value + unit
        if string is None:
            string = '0'
        string = '(' + string + ')'
        return string

