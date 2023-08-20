import math as m


def f(x):
    return x - 2 * m.log(x) - 5


def falsiPosition(a, b):
    for i in range(20):
        x = (a * f(b) - f(a) * b) / (f(b) - f(a))
        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        print('f(a): {0:.10f}\t f(b): {1:.10f}\t x: {2:.10f}\t '.format(f(a), f(b), x))


falsiPosition(0.01, 1)
