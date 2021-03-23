#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    suma = 0
    for x in ar:
        suma += x
    return suma, len(ar)

array = [1, 2, 3, 4, 10, 11]
print(simpleArraySum(array))
