import math


def FactorialOfN(num):
    result = num
    while num != 1:
        result = result * (num - 1)
        num = num - 1
    return result


def OptimizedFactorial(num):
    return (math.factorial(num))
