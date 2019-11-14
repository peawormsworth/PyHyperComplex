# PyHyperComplex

python class for Cayley Dickson number construction and operation.

### Usage:

from hypercomplex import Construction

a = Construction(1,2)

b = Construction(3,-1)

sum = a + b

difference = a - b

product = a * b

division = a / b

conjugate = a.conjugate()

inverse = 1/a = ~a

if a == b:
    print ("equal")


## Untested Features

power = a ** 2.1

log_of_a = a.log()

gn = a.geodesic_norm

a.complex()

t = a.tensor(b)

