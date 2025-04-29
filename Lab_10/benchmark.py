import time
def benchmark(arg):
    def _benchmark(f):
        def __benchmark(*args,**kw):
            if arg:
                t = time.perf_counter()
                rez = f(*args,**kw)
                t = time.perf_counter() - t
                print(f'Функція {f.__name__} працювала {t} секунд')
            else:
                rez = f(*args,**kw)
            return rez
        return __benchmark
    return _benchmark

b=True
@benchmark(b)
def fibonachi(n):
    f0,f1 = 1,1
    for i in range(2,n+1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f

def fibonachi_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonachi_rec(n-1) + fibonachi_rec(n-2)

c = False
@benchmark(c)
def fib_rec(n):
    return fibonachi_rec(n)

import math
@benchmark(c)
def factorial(n):
    return math.factorial(n)

print(fibonachi(30))
print(fib_rec(30))
print(factorial(30))
