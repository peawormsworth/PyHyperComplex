PyHyperComplex
===============

python class for Cayley Dickson number construction and operation.

Purpose:
--------

This is recreational/demonstration code. I use it to investigate code representing alternate algebras and to simulate gate operations on quantum states. The code can be used for anything where multidimensional calculations are required.

Usage:
------

from hypercomplex import Construction

``a = Construction(1,2)``

``b = Construction(3,-1)``

``sum = a + b``

``difference = a - b``

``product = a * b``

``division = a / b``

``conjugate = a.conjugate()``

``inverse = 1/a = ~a``

``if a == b:``

``    print ("equal")``

Output Options:
---------------

``A = Construction(1,2,3,4)``

``print ("A with imaginary units: ", a)``

``print ("A as list: ", A.flat())``

``from hypercomplex import RootFraction``

``x = 1 - sqrt(1/2) - sqrt(1/4) - sqrt(3/8)``

``A = RootFraction(sqrt(1/2),sqrt(1/4),sqrt(3/8),x)``

``print ("A as a root fraction list: A)``

Untested Features:
------------------

``power = a ** 2.1``

``log_of_a = a.log()``

``gn = a.geodesic_norm``

``a.complex()``

``t = a.tensor(b)``

