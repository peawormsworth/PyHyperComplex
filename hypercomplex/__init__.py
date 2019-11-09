import math
import random

class Construction(object):

    isquare   = -1
    PRECISION = 10 ** -9

    def __add__ (m, o):
        if o.__class__ == m.__class__:
            a, b = m.a + o.a, m.b + o.b
        else:
            a, b = m.a + o, m.b

        return m.__class__((a, b))

    def __radd__ (m, o):
        return m + o

    def __rsub__ (m, o):
        return (-m)+ o

    def __sub__ (m, o):
        return m + (-o)

    def __rmul__ (m, o):
        return m * o

    def __rtruediv__ (m, o):
        return ~m * o

    def __truediv__ (m, o):
        if o.__class__ == m.__class__:
            io = ~o
        else:
            io = 1/o
        return io * m

    def __mul__ (m, o):
        a  = m.a
        b  = m.b
        c  = o
        cs = o
        d  = 0
        ds = 0

        if hasattr(o, 'a'):
            c = o.a
            if hasattr(c, 'conj'):
                cs = c.conj()
            else:
                cs = c

        if hasattr(o, 'b'):
            d = o.b
            if hasattr(d, 'conj'):
                ds = d.conj()
            else:
                ds = d

        return m.__class__((a*c + m.isquare * ds*b, d*a + b*cs))

    def __abs__ (m):
        return math.sqrt(abs(m.a) ** 2 + abs(m.b) ** 2)

    def __invert__ (m):
        return m.conj() / (abs(m) ** 2)

    def __pow__ (m):
        return math.exp(m.re) * (math.cos(abs(m.im)) + m.im.normalize * math.sin(abs(m.im)))

    def __neg__ (m):
        return -1 * m

    def __pos__ (m):
        return m

    # is this right? should we return a new object or should we be modifying the content of the existing one?
    # this is NOT RIGHT. I need to perform ASSIGNMENT and I can't do this until I know python better. sad is me.
    def __iadd__ (m, o):
        return m + o

    def __isub__ (m, o):
        return m - o

    def __imul__ (m, o):
        return m * o

    def __idiv__ (m, o):
        return m / o

    def __ipow__ (m, o):
        return m ** o

    def __eq__ (m, o):
        (m - o).norm() <= PRECISION

    def __ne__ (m, o):
        not m == o

    def __complex__ (m):
       return PyComplex_FromDoubles( float(abs(m.a)), float(abs(m.b)) )

    def log (m):
        return math.log(abs(m)) + m.im().normalize() * math.acos(m.re() / abs(m))

    def conj (m):
        if m.is_complex:
            a, b = m.a, -m.b
        else:
            a, b = m.a.conj(), -m.b

        return m.__class__((a, b))

    def norm (m):
        return abs(m)

    def normalize (m):
        abs(m)
        return m / abs(m)

    def geodesic_norm (m, o):
        return abs((o/m).log)

    def tensor (m, o):
        if m.is_complex:
            return m * o
        else:
            return m.__class__((m.a.tensor(o), m.b.tensor(o)))

    def __getitem__ (m, index):
        return m.flat()[index]

    def flat (m):
        if m.is_complex():
           return m.a, m.b
        else:
           return m.a.flat() + m.b.flat()

    def __getitem__ (m, index):
        return m.flat()[index]

    def flat (m):
        if m.is_complex:
           return (m.a, m.b)
        else:
           return (m.a + m.b)

    def __repl__ (m):
        return m.__class__.__name__ + '(' + ','.join(str(x) for x in m) + ')'

    def __str__ (m):
        string = ''
        if abs(m):
            for index, t in enumerate(m):

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


    def is_real             (m): return abs(m - m.conj()) == 0
    def is_complex          (m): return type(m.a) is Number
    def is_quaternion       (m): return not m.is_complex() and m.a.is_complex()
    def is_octonion         (m): return not m.is_complex() and m.a.is_quaternion()
    def is_sedenion         (m): return not m.is_complex() and m.a.is_octonion()
    def is_trigintaduonions (m): return not m.is_complex() and m.a.is_sedenion()

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

    def a (m, a=None):
        if a is not None:
            m.a = a
        return m.a

    def b (m, b=None):
        if b is not None:
            m.b = b
        return m.b

    def re (m):
        return m[0]

    def im (m):
        return m.__class__((0,(m[1:])))


