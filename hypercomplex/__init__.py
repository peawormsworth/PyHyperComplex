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

    def __add__ (m, o):
        try:
            a, b = m.a + o.a, m.b + o.b
        except:
            a, b = m.a + o, m.b

        return m.__class__((a, b))



    #
    # reverse Addition
    #

    def __radd__ (m, o):
        return m + o



    #
    # referse Subtract
    #

    def __rsub__ (m, o):
        return -m + o


    #
    # Subtraction: (a,b)-(c,d) = (a-c,b-d)
    #

    def __sub__ (m, o):
        return m + -o



    #
    # Reverse Multiplication
    #

    def __rmul__ (m, o):
        return m * o



    #
    # Reverse Division
    #

    def __rtruediv__ (m, o):
        return ~m * o



    #
    # Division: z1/z2 = (a,b) × (c,d)⁻¹ = (a,b) × inverse(c,d)
    #

    def __truediv__ (m, o):
        if isinstance(o, Construction):
            return  ~o * m
        else:
            return 1/o * m



    #
    # Multiplication: (a,b)×(c,d) = (a×c - d*×b, d×a + b×c*) 
    #   where x* = conjugate(x) or x if x is a number
    #

    def __mul__ (m, o):
        a  = m.a
        b  = m.b

        try:
            c = o.a
        except:
            c = o

        try:
            d = o.b
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

        return m.__class__(m.doubling_product(a,b,c,d,ac,bc,cc,dc))



    #
    # Doubling Product: multiplication rules for (a,b)×(c,d)
    #   given the values a,b,c,d,a★,b★,c★,d★
    #  where x★ = conjugate of x
    #

    def doubling_product (m,a,b,c,d,ac,bc,cc,dc):
        return (a*c + m.isquare * dc*b, d*a + b*cc)



    #
    # Absolute Value = Norm: √(norm(a)²+norm(b)²)
    #

    def __abs__ (m):
        return math.sqrt(abs(m.a) ** 2 + abs(m.b) ** 2)



    #
    # Invert: z⁻¹
    #

    def __invert__ (m):
        return m.conj()  / abs(m) ** 2



    #
    # Power: z^x
    #

    def __pow__ (m, power):
        return abs(m) ** power * (math.cos(power * abs(m.im())) + m.im().normalize() * math.sin(power * abs(m.im())))



    #
    # Negate: -z = -1 × z
    #

    def __neg__ (m):
        return -1 * m



    #
    # Positive: +z = z
    #

    def __pos__ (m):
        return m



    #
    # Replace: the existing coefficients with those of the given one
    #

    def replace (m, o):
        m.a(o.a)
        m.b(o.b)
        return m



    #
    # Addition with assignment: z += x
    #

    def __iadd__ (m, o):
        return m.replace(m.__add__(o))



    #
    # Subtraction with assignment: z -= x
    #

    def __isub__ (m, o):
        return m.replace(m.__sub__(o))



    #
    # Multiplication with assignment: z *= x
    #

    def __imul__ (m, o):
        return m.replace(m.__mul__(o))



    #
    # Division with assignment: z /= x
    #

    def __idiv__ (m, o):
        return m.replace(m.__div__(o))



    #
    # Power with assignment: z **= x
    #

    def __ipow__ (m, o):
        return m.replace(m.__pow__(o))



    #
    # Equality condition: true if z = x
    #

    def __eq__ (m, o):
        return (m - o).norm() <= m.precision



    #
    # Inequality: true is z ≠ x
    #

    def __ne__ (m, o):
        return not m == o



    #
    #  automatically generate a Complex object using the weight of a and b 
    #    as the real and imaginary components
    #

    def __complex__ (m):
       return complex( float(abs(m.a)), float(abs(m.b)) )



    #
    #  the power to which e mush be raised to obtain this number
    #  if this number is z, then log(z) returns the x, so that e^x = z
    #  Log: log(z) = x, so that e^x = z
    #

    def log (m):
        return math.log(abs(m.im())) + m.im().normalize() * math.acos(m.re() / abs(m))



    # 
    #  Conjugate: z* = (a,b)* = (a*,-b)
    #

    def conj (m):
        try:
            ac = m.a.conj()
        except:
            ac = m.a
        return m.__class__((ac, -m.b))



    #
    # Norm: √(norm(a)²+norm(b)²) and norm(number) = number
    #

    def norm (m):
        return abs(m)



    #
    # Normalize: z/|z| = zn, where norm of zn = 1
    #

    def normalize (m):
        return m / abs(m)



    #
    # Geodesic Norm: gn(z,x) = |ln(z⁻¹x)|
    # ref: https://en.wikipedia.org/wiki/Quaternion#Geodesic_norm
    #

    def geodesic_norm (m, o):
        return abs(log(~m * o))

        # although there is no symbol in our math for it...
        # this is equivelent to right division...
        #
        # return abs(log(m.__rtruediv__(o)))

    #
    # Tensor: $a->tensor($b) = A ⊗ B = (a,b) ⊗ (c,d) = (ac,ad,bc,bd)
    #

    def tensor (m, o):
        try:
            return m.__class__((m.a.tensor(o), m.b.tensor(o)))
        except:
            return m.__class__((o * m.a,  o * m.b))



    #
    # return dimension count for this number
    #

    def dimension(m):
        return len(m.flat())



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

    def level (m):
        return math.log(m.dimension())/math.log(2)



    #
    # confirm the imaginary portions of the number are zero
    #

    def is_real (m):
        return not m.im



    #
    # confirm this number is a 2d Complex number
    #

    def is_complex (m):
        return m.level() == 1



    #
    # confirm this number is a 4d Quaternion number
    #

    def is_quaternion  (m):
        return m.level() == 2



    #
    # confirm this number is a 8d Octonion number
    #

    def is_octonion (m):
        return m.level() == 3



    #
    # confirm this number is a 16d Sedenion number
    #

    def is_sedenion (m):
        return m.level() == 4



    #
    # initialize a new object request
    #   expects a 2^n element tuple parameter
    #

    def __init__ (m, list):

        h = len(list) // 2
        if h > 1:
            m.a(m.__class__((list[:h])))
            m.b(m.__class__((list[h:])))
        elif h < 1:
            m.a(list[0])
            m.b(0)
        else:
            m.a(list[0])
            m.b(list[1])



    #
    # a: left half of number
    #

    def a (m, a=None):
        if a is not None:
            m.a = a
        return m.a



    #
    # b: right half of number
    #

    def b (m, b=None):
        if b is not None:
            m.b = b
        return m.b



    #
    # Real part of number
    #

    def re (m):
        return m[0]



    #
    # Imaginary part of number
    #

    def im (m):
        return m.__class__(((0,) + m[1:]))



    #
    # return the coefficient of the basis for the provided index
    #

    def __getitem__ (m, i):
        return m.flat()[i]



    #
    # return an ordered list of the coefficients
    #

    def flat (m):
        try:
           return m.a.flat() + m.b.flat()
        except:
           return (m.a, m.b)



    #
    # String format:
    #   ordered imaginary units: i, j, k, etc.
    #   no basis is shown for real units
    #   no leading positive symbol
    #

    def __str__ (m):
        string = ''
        if abs(m):

            for index, coefficient in enumerate(m.flat()):

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

    def __repr__ (m):
        return "%r(%r)" % ( str(m.__class__.__name__), m[::] )


from fractions import Fraction

class RootFraction(Construction):

    def __str__ (m):
        string = ''
        if abs(m):

            for index, coefficient in enumerate(m.flat()):

                if coefficient != 0: 
                    sign = ''
                    if coefficient < 0: 
                        sign = '-'
                    elif len(string):
                        sign = '+'

                    if string != '':
                        sign = ' ' + sign + ' '

    
                    if index:
                        unit = '·e' + str(index)
                    else:
                        unit = ''

                    #value = abs(coefficient)
                    #rootfraction = Fraction.from_float(float(abs(coefficient) ** 2))
                    fraction = Fraction.from_float(float(abs(coefficient) ** 2)).limit_denominator(1000000)

                    value = '√%s/%s' %  (fraction.numerator, fraction.denominator)

                    if value == '√1/1':
                        if unit == '':
                            value = '1'
                        else:
                            value = ''

                    string = string + sign + value + unit
                    #string = string + sign + '√' + unit

        if string is None:
            string = '0'

        string = '(' + string + ')'
        return string



