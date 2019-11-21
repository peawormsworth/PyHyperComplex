# HyperComplex

HyperComplex makes multi-dimensional [Cayley-Dickson number][cayley_dickson] calculations easy.
Calculate to dimensions of any size with intuitive and fully overloaded math
operation.

[The source of this project is available here][src].

Structure
---------

Each object has two things, a and b, which are either two numbers or two
similar objects. The object is a tree contain a total of 2^depth numbers.
The total of numbers is the dimension. These numbers represent the coefficients
of a Cayley-Dickson number of that dimension.

Usage
-----

general operation...

    from hypercomplex import Construction

    q1 = Construction( 4, 2, 3, 7)

    q2 = Construction(-1, 0.5, 2, 6)

    sum = c1 + c2

    difference = c1 - c2

    product = c1 * c2

    division = c1 / c2

store product in c1

    c1 *= c2

other features...

    norm = abs(c1)

    invert = ~ c1

    root = c1 ** 0.5

    negative = -c1

    if c1 == c2:

        print ("equal")

    complex_type = c1.complex()

    logarithm = c1.log()

    as_a_list = c1[::]

    conjugate = c1.conj()

    arc_distance = c1.geodesic_norm(c2)

    quaternion = c1.tensor(c2)

    if c1.dimension == 4:

        print ("I am a Quaternion")

    if c1.is_real:

        print ("I am entirely real")

    if c1.is_complex:

        print ("I am a 2 dimensional complex number")

for more detailed examples look in to test_hypercomplex.py

Related Topics
--------------

[Cayley-Dickson numbers][cayley_dickson]
[Complex numbers][complex]
[Quaternions][quaternion]
[Octonions][octonion]
[Sedenions][sedenion]

Progress
--------

This work in progress is educational code. It is designed to follow the
structure and produess of Cayley Dickson algebra as a recursive process.
process during hyperdimensional math operations. This code is not designed 
to be efficient. This is educational code.

[src]: https://github.com/peawormsworth/PyHyperComplex
[cayley_dickson]: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
[complex]: https://en.wikipedia.org/wiki/Complex_number
[quaternion]: https://en.wikipedia.org/wiki/Quaternion
[octonion]: https://en.wikipedia.org/wiki/Octonion
[sedenion]: https://en.wikipedia.org/wiki/Sedenion
