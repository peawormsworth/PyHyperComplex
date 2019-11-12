#!/usr/bin/python3
#
#  Simulate Quantum Operations
#
#     file: t5_quantum.py
#   source: https://github.com/peawormsworth/PyHyperComplex
#   author: Jeffrey B Anderson - truejeffanderson at gmail.com
#
#     reference: https://www.microsoft.com/en-us/research/video/quantum-computing-computer-scientists
#


import hypercomplex

from hypercomplex import Construction
from random       import random
from math         import sqrt


LOOPS = 20
PRECISION = 10 ** -9


#
# generate a random complex number ...
#

def random_vector ():
    return Construction((
        random(), random(), random(), random(), random(), random(), random(), random(), 
        random(), random(), random(), random(), random(), random(), random(), random(), 
    ))



print ("\nInstantiate state tests...\n")

instantiate = [
   [ Construction((1,2)), (1,2) ],
   [ Construction((3,4)), (3,4) ]
]

expect = (1,2)

for entry in instantiate:
    calc, expect = entry[::]

    print ("\nVerify %s = %s" % (repr(calc), expect))
    print ("       calc : ", calc)
    print ("       calc : ", calc.flat())
    print ("     expect : ", expect)

    if calc.flat() == expect:
        print ("Success\n")
    else:
        print ("    diff: ", (calc - expect).flat())
        print ("Fail\n")
        exit()


#
# Tensor tests
#

print ("\nTensor tests...\n")


z1 = Construction((1,2))
z2 = Construction((3,4))


# setup zero (z) and one (o)
z = Construction((1,0))
o = Construction((0,1))


brakets = [
    [ 'Verify (1,2) ⊗ (3,4) = (3,4,6,8)', z1.tensor(z2), (3,4,6,8) ],

    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |100>', o.tensor(z.tensor(z)), (0,0,0,0,1,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (0,1) = |101>', o.tensor(z.tensor(o)), (0,0,0,0,0,1,0,0) ],
    [ 'Verify (0,1) ⊗ (0,1) ⊗ (1,0) = |110>', o.tensor(o.tensor(z)), (0,0,0,0,0,0,1,0) ],
    [ 'Verify (0,1) ⊗ (0,1) ⊗ (0,1) = |111>', o.tensor(o.tensor(o)), (0,0,0,0,0,0,0,1) ],

    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1000>', o.tensor(z.tensor(z.tensor(z))), (0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1001>', o.tensor(z.tensor(z.tensor(o))), (0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1010>', o.tensor(z.tensor(o.tensor(z))), (0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1011>', o.tensor(z.tensor(o.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1100>', o.tensor(o.tensor(z.tensor(z))), (0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1101>', o.tensor(o.tensor(z.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1110>', o.tensor(o.tensor(o.tensor(z))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |1111>', o.tensor(o.tensor(o.tensor(o))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1) ],

    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10000>', o.tensor(z.tensor(z.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10001>', o.tensor(z.tensor(z.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10010>', o.tensor(z.tensor(z.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10011>', o.tensor(z.tensor(z.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10100>', o.tensor(z.tensor(o.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10101>', o.tensor(z.tensor(o.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10110>', o.tensor(z.tensor(o.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |10111>', o.tensor(z.tensor(o.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11000>', o.tensor(o.tensor(z.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11001>', o.tensor(o.tensor(z.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11010>', o.tensor(o.tensor(z.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11011>', o.tensor(o.tensor(z.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11100>', o.tensor(o.tensor(o.tensor(z.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11101>', o.tensor(o.tensor(o.tensor(z.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11110>', o.tensor(o.tensor(o.tensor(o.tensor(z)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0) ],
    [ 'Verify (0,1) ⊗ (1,0) ⊗ (1,0) = |11111>', o.tensor(o.tensor(o.tensor(o.tensor(o)))), (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1) ],
]

for item in brakets:
    title, calc, expected = item
    expect = Construction(expected)

    print (title)
    #print ("       calc : ", calc)
    print ("       calc : ", calc.flat())
    print ("     expect : ", expect.flat())

    #if calc.flat() == expect.flat():
    if calc == expect:
        print ("Success\n")
    else:
        print ("difference:", abs(calc - expect))
        print ("Fail\n")
        exit()



gate_cnot     = Construction((sqrt(1/2), sqrt(1/2),0,0))
gate_x        = Construction((0, 1))
gate_hadamard = Construction((sqrt(1/2), sqrt(1/2)))

def cnot(z1,z2):
    c = z1.tensor(z2)
    return gate_cnot * c * ~ gate_cnot


#def xgate(z):
#    return gate_x * z / gate_x
    
def xgate(z):
    return gate_x / z 
    
def hadamard(z):
    return gate_hadamard / z
    
#
# Bra-Ket Notation reference table
#

print ("\nBra-Ket notation reference:\n")

zz = z.tensor(z)
zo = z.tensor(o)
oz = o.tensor(z)
oo = o.tensor(o)
rz = hadamard(z)
ro = hadamard(o)


print (" |0|> = %s = %s" % ( z.flat(),  z))
print (" |1|> = %s = %s" % ( o.flat(),  o))
print ("|00|> = %s = %s" % (zz.flat(), zz))
print ("|01|> = %s = %s" % (zo.flat(), zo))
print ("|10|> = %s = %s" % (oz.flat(), oz))
print ("|11|> = %s = %s" % (oo.flat(), oo))
print (" |+|> = %s = %s" % ( rz.flat(),  rz))
print (" |-|> = %s = %s" % ( ro.flat(),  ro))



#
# XGATE: Flip along √i axis. 1 => 0, 0 => 1
#

print ("\n\nXGATE truth table:\n")

cnot_tests = [
    [ 'Verify XGATE +|0>| = +|1>', xgate( z),  o ],
    [ 'Verify XGATE +|1>| = +|0>', xgate( o),  z ],
    [ 'Verify XGATE -|0>| = -|1>', xgate(-z), -o ],
    [ 'Verify XGATE -|1>| = -|0>', xgate(-o), -z ],
    [ 'Verify XGATE |00>| = -|0>', xgate(zz), oz ],
    [ 'Verify XGATE |01>| = -|0>', xgate(zo),-oo ],
    [ 'Verify XGATE |10>| = -|0>', xgate(oz), zz ],
    [ 'Verify XGATE |11>| = -|0>', xgate(oo), zo ],
]

for test in cnot_tests:
    title, calc, expect = test

    print (title)
    print ("       calc : ", calc.flat())
    print ("     expect : ", expect.flat())

    if calc == expect:
        print ("Success\n")
    else:
        print ("difference:", abs(calc - expect))
        print ("Fail\n")
        exit()



#
# CNOT: second bit flip controlled by the first
#

print ("\nCNOT truth table:\n")

cnot_tests = [
    [ 'Verify CNOT |00>| =  |00>', cnot(z,z), (1, 0, 0, 0) ],
    [ 'Verify CNOT |01>| =  |01>', cnot(z,o), (0, 1, 0, 0) ],
    [ 'Verify CNOT |10>| =  |11>', cnot(o,z), (0, 0, 0, 1) ],
    [ 'Verify CNOT |11>| = -|10>', cnot(o,o), (0, 0,-1, 0) ]
]

for test in cnot_tests:
    title, calc, expected = test
    expect = Construction(expected)

    print (title)
    print ("       calc : ", calc.flat())
    print ("     expect : ", expect.flat())

    if calc == expect:
        print ("Success\n")
    else:
        print ("difference:", abs(calc - expect))
        print ("Fail\n")
        exit()


#
# Hadamard gate
#

print ("\nHadamard truth table:\n")

hadamard_tests = [
    [ 'Verify HADAMARD +| 0>| = + | +>', hadamard( z), rz ],
    [ 'Verify HADAMARD +| 1>| = + | ->', hadamard( o), ro ],
    [ 'Verify HADAMARD -| 0>| = - | +>', hadamard(-z),-rz ],
    [ 'Verify HADAMARD -| 1>| = - | ->', hadamard(-o),-ro ],
    [ 'Verify HADAMARD +|00>| = + |1+>', hadamard(zz), rz.tensor(z) ],
    [ 'Verify HADAMARD +|01>| = - |11>', hadamard(zo), -rz.tensor(o) ],
    [ 'Verify HADAMARD +|10>| = + |00>', hadamard(oz), ro.tensor(z) ],
    [ 'Verify HADAMARD +|11>| = + |01>', hadamard(oo), ro.tensor(o) ],
]

for test in hadamard_tests:
    title, calc, expect = test

    print (title)
    print ("       calc : ", calc.flat())
    print ("     expect : ", expect.flat())

    if calc == expect:
        print ("Success\n")
    else:
        print ("difference:", abs(calc - expect))
        print ("Fail\n")
        exit()



#
# 16 Step Circle Walk test
#

z = Construction((1,0))

print ("\n16 Steps around the Unit Circle:\n")


print ("Starting:", z.__repl__())
for i in range(16):

    if i % 2:
        gate = 'Hadamard'
        z2 = hadamard(z)
    else:
        gate = 'XGate'
        z2 = xgate(z)

    print ("  Step %s: %s(%s) = (%s) = %s" % (i+1, gate, z, z2.flat(), z2))
    z = z2
print ("   Ending: %s\n" % (z.__repl__()))



#
# Black box gate actions: constant 0, constant 1, identity and negate
#

# NOTE: This test is incomplete

print ("\nBlack box gate action test:\n")

box_tests = [
    [ 'Constant-0 |--> =  |11>', 'constant_0', o,  o ],
    [ 'Constant-1 |--> = -|11>', 'constant_1', o, -o ],
    [ '  Identity |--> =  |00>', 'identity',   z,  o ],
    [ '    Negate |--> =  |01>', 'negate',     z, -o ],
]

print ("recall: H(X(|0>)) ⊗ H(X(|0>))  =  |->| ⊗ |->|  =  |-->\n\n\n")

for test in box_tests:
    title, action, expect_control, expect_target = test

    control = z
    target  = z

    control = xgate(control)
    target  = xgate(target)
    
    control = hadamard(control)
    target  = hadamard(target)
    
    if action == 'constant_1' or action == 'negate':

        print ("\nApplying XGate to target")
        print (" orig target: ", target)
        target = xgate(target)
        print ("  new target: ", target)

    if action == 'identity' or action == 'negate':

        print ("\nApplying CNOT Gate")
        print (" orig target: ", target)
        print (" orig control:", control)

        calc = cnot(control,target)

        # now how do I extrac control and target from the combine calculated output?
        print ("# now how do I extract control and target from the combine calculated output?")


        print ("  new state: ", calc)

    control = hadamard(control)
    target  = hadamard(target)

    print (title + "\n")

    print ("   calc control : ", control.flat())
    print (" expect control : ", expect_control.flat())

    if control == expect_control:

        print ("Success\n")

    else:

        print ("difference:", abs(control - expect_control))
        print ("Fail\n")
        #exit()


    print ("   calc target : ", target.flat())
    print (" expect target : ", expect_target.flat())

    if target == expect_target:

        print ("Success\n")

    else:

        print ("difference:", abs(target - expect_target))
        print ("Fail\n")
        #exit()




