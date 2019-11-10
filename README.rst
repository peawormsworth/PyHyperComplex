HyperComplex
============

HyperComplex makes multi-dimensional Cayley-Dickson number calculations easy.
Calculate to dimensions of any size with intuitive and fully overloaded math operation.


Usage
-----

Create:

import hypercomplex
from hypercomplex import Construction

c1 = Construction( 4, 2)
c2 = Construction(-1, 0.5)

quaternion = Construction(1,2,3,4)
octonion   = Construction(-1,7,6,5,8,3,2,4)

Display:

print ("c1 = ", c1)
print ("c2 = ", c2.flat())
print ("Quaternion = ", quaternion)
print ("Octonion   = ", c1.flat())

Calculate:

product     = c1 * c2
difference  = c1 - c2
equality    = c1 == c2
q_norm      = abs(quaternion)
o_normalize = octonion.normalize
c2_inverse  = ~ c2
c1_squared  = c1 ** 2
root_c2     = c2 ** 0.5
log_o       = log(o)
negative_c1 = -c1

# negate c1 and store it back into itself ...
c1 *= -1

# the 3rd element of the octonion...
element3 = octonion[2]

etc...


Status
------

Work in progress. Expect frequent and total changes.

