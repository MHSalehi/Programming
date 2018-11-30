# ----------------------------------------------------------------------------------------------------------------------
# 1.)Functions
# ----------------------------------------------------------------------------------------------------------------------

# a = "Hello"
# b = None

# def print_hello(a):
#     b = 0
#     print(a)
#     print(len(a))
#     for i in range(len(a)):
#         if a[i] == "l":
#             b += 1
#     print(b)
#
#
#
# print_hello("Hello")               # Calls the defined 'print_hello()'function above.
#
# l = [1, 2, 4, 6, 8]
#
# def multiply2(a):
#     b = []
#     for i in a:
#         b.append(i*2)
#     print(b)
#
# multiply2(l)
#
#
#
# def addition(a,b):
#     return a + b
#
#     x = addition(5,5)
#     print(x)
#
# addition(5,5)
#
#
#
# a = 4
#
# def valueInsideFunction():
#     a =17
#     print("Value of a inside function:", a)
#
# valueInsideFunction()
# print("Value of a outside Function", a)
#
# a = 4
#
#
# def valueInsideFunction():
#     global a
#     a = 17                          // Overwrites the global value
#     print("Value of a inside function:", a)
#
#
# valueInsideFunction()
# print("Value of a outside Function", a)



import Class6ImportFileTest

print(Class6ImportFileTest.addition(2,9))



from Class6ImportFileTest import addition           # Means you dont need to use the '.<function>' call above
                                                    # Can use 'addition' alone

from Class6ImportFileTest import *                  # Imports ALL functions from the file. Will import global values.


import Class6ImportFileTest as shortname            # Can import and rename a file for easy reference e.g. 'shortname'


# ----------------------------------------------------------------------------------------------------------------------
# 2.) Random Module
#  ----------------------------------------------------------------------------------------------------------------------

import random

random.randint(a,b)             # Generates a random integer between a, b
random.uniform(a,b)             # Generates random float between a,b
random.chjoice(seqeuence)       # Generates random value from a non empty sequence

