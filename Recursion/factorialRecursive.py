# def recursiveFunction(num):
#     if Base Condition:
#         return ----
#     else:
#         Recursive Condition
#         return num + accumulativeSum(num-1)


import sys


def factorial(num):
    if (num == 0):
        return 0
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)


def accumulativeSum(num):
    if (num == 0):
        return 0
    else:
        return num + accumulativeSum(num-1)


print('Factorial is -> ', factorial(5))
print('Accumulative Sum is -> ', accumulativeSum(5))


print('System Recursive Limit -> ', sys.getrecursionlimit())
print('Python version -> ', sys.version)
