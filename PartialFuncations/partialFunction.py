from functools import partial


def fun(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


var = partial(fun, 1, 2)
var1 = partial(fun, c=1, d=2)

print(var(4, 5))
print(var1(4, 5))
