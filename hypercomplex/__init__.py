#
#   hypercomplex.Construction
#
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     based off: https://github.com/peawormsworth/Cayley-Dickson
#     reference: https://en.wikipedia.org/wiki/Cayley-Dickson_construction
#

import math

# todo: this program depends on type checking.
#   Apparently this ins not the python way.
#   Is there a more standard way to achieve this effect?

# todo: do we need to subclass object?
#class Construction(object):
class Construction:

    isquare = -1
    PRECISION = 10 ** -9

    def __add__ (m, o):
        try:
            a, b = m.a + o.a, m.b + o.b
        except:
            a, b = m.a + o, m.b

        return m.__class__((a, b))


    def __radd__ (m, o):
        return m + o


    def __rsub__ (m, o):
        return -m+ o


    def __sub__ (m, o):
        return m + -o


    def __rmul__ (m, o):
        return m * o


# todo: is the disions in the right order for sure?
    def __rtruediv__ (m, o):
# todo: verify inverse before multiplication ordering or add brackets...
        return ~m * o


    def __truediv__ (m, o):
        if isinstance(o, Construction):
            return  ~o * m
        else:
            return 1/o * m


# todo: multiplication ordering is not standardized.
# are we using correct orders or should we swap. or make it a setting choice?
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

        return m.__class__((a*c + m.isquare * dc*b, d*a + b*cc))


# there is a short form for this. We could just square the coefficients add and take the root ...
# this method is cool because it doesn't assume a standard structure...
    def __abs__ (m):
        return math.sqrt(abs(m.a) ** 2 + abs(m.b) ** 2)


# note: order of multiplication is not important since one side is real ...
    def __invert__ (m):
        return m.conj() * (1 / (abs(m) ** 2))


# todo: this doesn't work at all. Figure this out.
# it is based on quaternion powers formula from wikipedia.
# Search there to see what it should be.
# todo: this can't be right. I guessed as some of this...
    def __pow__ (m, power):
        rm = m[0]
        im = m.__class__(((0,) + m[1:]))
        #print ("rm: ", rm)
        #print ("im: ", im.flat())
        return abs(m) ** power * (math.cos(power * abs(im)) + im.normalize() * math.sin(power * abs(im)))
        #return math.exp(rm) * (math.cos(abs(im)) + im.normalize * math.sin(abs(im)))


    def __neg__ (m):
        return -1 * m


    def __pos__ (m):
        return m


# todo: verify this works and test all the auto replace operations i*
    def replace (m, o):
        m.a(o.a)
        m.b(o.b)
        return m


    def __iadd__ (m, o):
        return m.replace(m.__add__(o))


    def __isub__ (m, o):
        return m.replace(m.__sub__(o))


    def __imul__ (m, o):
        return m.replace(m.__mul__(o))


    def __idiv__ (m, o):
        return m.replace(m.__div__(o))


    def __ipow__ (m, o):
        return m.replace(m.__pow__(o))


    def __eq__ (m, o):
        return (m - o).norm() <= m.precision()


    def __ne__ (m, o):
        return not m == o


# todo: complex is totally untested and no idea how to test.
#    if you know how coComplex pi numbers work... you may check this.
# note: if the object is more than complex dimensions, 
#    it will flatten it to its two dimensional probabilities 
#    (it's root sum of squares) for each of the two branches 
#    of the provided object.

    def __complex__ (m):
       return PyComplex_FromDoubles( float(abs(m.a)), float(abs(m.b)) )


# todo: untested. m.im and m.re are suspect too...
    def log (m):
        rm = m[0]
        im = m.__class__(((0,) + m[1:]))
        #print ("rm: ", rm)
        #print ("im: ", im.flat())
        return math.log(abs(m)) + im.normalize() * math.acos(rm / abs(m))


    def conj (m):
        try:
            ac = m.a.conj()
        except:
            ac = m.a
        return m.__class__((ac, -m.b))


    def norm (m):
        return abs(m)


    def normalize (m):
        return m / abs(m)


    def geodesic_norm (m, o):
        return abs((o/m).log)


    def tensor (m, o):
        try:
            return m.__class__((m.a.tensor(o), m.b.tensor(o)))
        except:
            return m * o


# todo: i put this in and think it works. But I don't know if it's used or works as intended. Must first understand and then test.
# note: it seems to work now like this for some reason...
    def __getitem__ (m, i):
        return m.flat()[i]


    def flat (m):
# todo: we have the __getitem__ iterable default. Could we just call m[::] instead ???
        #m[::]
        try:
           return m.a.flat() + m.b.flat()
        except:
           return (m.a, m.b)


# todo: test this if you want JSON dumping and object creation ...
    def __repl__ (m):
        return m.__class__.__name__ + '(' + ','.join(str(x) for x in m) + ')'


# this is one output form. It uses i,j,k,l,... for imaginary units
# no basis is shown for real units
# no leading +
    def __str__ (m):
        string = ''
        if abs(m):

            for index, t in enumerate(m.flat()):

                sign = ''
                if t < 0: 
                    sign = '-' 
                elif len(string):
                    sign = '+'

                value = 0
                if not(abs(t) == 1 and index):
                    value = abs(t)

                unit = chr(ord('i') + index)

                string = string + sign + str(value) + unit

        if string is None:
            string = '0'

        return string


# This is not saying that the object has 0 in the imaginary part
# I have defined it more mathematically and I am unsure if it is totally true.
    def is_real (m):
        return m == m.conj()
# an alternate form may be ...
        #return not abs(m.b)


# todo: is it simpler just to count the dimensions?
# ie:
    def X_is_complex (m):
        return m.dimension() == 2

    def X_is_quaternion  (m):
        return m.dimension() == 4

    def X_is_octonion (m):
        return m.dimension() == 8

    def X_is_sedenion (m):
        return m.dimension() == 16 

    def is_complex (m):
        return not isinstance(m.a, Construction)


    def is_quaternion (m):
        return not m.is_complex() and m.a.is_complex()


    def is_octonion (m):
        return not m.is_complex() and m.a.is_quaternion()


    def is_sedenion (m):
        return not m.is_complex() and m.a.is_octonion()


# todo: is this a real name? I heard it somewhere and put it here, but I don't think it is standard. remove?
    def is_trigintaduonions (m):
        return not m.is_complex() and m.a.is_sedenion()

    def dimension(m, c):
        try:
            return m.dimension() == c
        except:
            return len(m.flat())


    def __init__ (m, list, p=PRECISION):
        m.precision(p)
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


    def a (m, a=None):
        if a is not None:
            m.a = a
        return m.a


    def b (m, b=None):
        if b is not None:
            m.b = b
        return m.b


    def precision (m, p=None):
        if p is not None:
            m.p = p
        return m.p


    def re (m):
        return m[0]


    def im (m):
        print ("m[1:] : ", m[1:])
        return m.__class__((0,(m[1:])))

