# HyperComplex

HyperComplex makes multi-dimensional [Cayley-Dickson number][cayley_dickson] calculations easy.
Calculate to dimensions of any size with intuitive and fully overloaded math
operation.

[The source of this project is available here][src].

[Project Hosting][project]

Structure
---------

Each object has two things, a and b, which are either two numbers or two
similar objects. The object is a tree contain a total of 2^depth numbers.
The total of numbers is the dimension. These numbers represent the coefficients
of a Cayley-Dickson number of that dimension.

Usage
-----

basic operations...

    from hypercomplex import Construction

    q1 = Construction( 4, 2, 3, 7)

    q2 = Construction(-1, 0.5, 2, 6)

    sum = c1 + c2

    difference = c1 - c2

    product = c1 * c2

    division = c1 / c2

operations with assignment...

    c1 += c2

    c1 -= c2

    c1 *= c2

    c1 /= c2

advanced features...

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

further examples provided in [test_hypercomplex.py][test_code]

Related Topics
--------------

[Cayley-Dickson numbers][cayley_dickson]

[Complex numbers][complex]

[Quaternions][quaternion]

[Octonions][octonion]

[Sedenions][sedenion]

Progress
--------

This project is a work in progress. It is designed to mimic the structure
of Cayley Dickson algebra as a recursive process for hyperdimensional math
operations. This code is not efficient. This is educational code.

[src]: https://github.com/peawormsworth/PyHyperComplex
[test_code]: https://github.com/peawormsworth/PyHyperComplex/blob/master/test_hypercomplex.py
[project]: https://test.pypi.org/project/hypercomplex-peasworth/
[cayley_dickson]: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
[complex]: https://en.wikipedia.org/wiki/Complex_number
[quaternion]: https://en.wikipedia.org/wiki/Quaternion
[octonion]: https://en.wikipedia.org/wiki/Octonion
[sedenion]: https://en.wikipedia.org/wiki/Sedenion
