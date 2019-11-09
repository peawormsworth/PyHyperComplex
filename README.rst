HyperCompplex
=============

HyperComplex provides a multi-dimensional Cayley-Dickson number calculator.
It is easy to generate hypercomplex numbers of any 2^n dimensions.
Add, subtract, multiiply and divide objects with overloaded math operations (just use: + - * /)
Norm of any number is: 
   asb(object)
Inverse of any number is:
   ~ object

Untested features
-----------------
- Find powers (z^x) with: object ** x
- easily switch objects between sign and doubling products. ie: Dual, Split and Bi-complex numbers
- left vs right multiplication
- self modifying overloading needs real work ( += *=, etc)
- test, test, test -> move to real test suite
- only complex numbers (2 dimensional) numbers work. The init function does not handle larger sets of numbers. The problem is the recursive function which needs to create a list of lists. I can't seem to get the lists to join right. I just don't understand iteratable sets and lists and their differences.


